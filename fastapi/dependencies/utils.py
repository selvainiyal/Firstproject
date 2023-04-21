import dataclasses
import inspect
from contextlib import contextmanager
from copy import copy, deepcopy
from typing import (
    Any,
    Callable,
    Coroutine,
    Dict,
    ForwardRef,
    List,
    Mapping,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
    cast,
)

import anyio
from fastapi import params
from fastapi.concurrency import (
    AsyncExitStack,
    asynccontextmanager,
    contextmanager_in_threadpool,
)
from fastapi.dependencies.models import Dependant, SecurityRequirement
from fastapi.logger import logger
from fastapi.security.base import SecurityBase
from fastapi.security.oauth2 import OAuth2, SecurityScopes
from fastapi.security.open_id_connect_url import OpenIdConnect
from fastapi.utils import create_response_field, get_path_param_names
from pydantic import BaseModel, create_model
from pydantic.error_wrappers import ErrorWrapper
from pydantic.errors import MissingError
from pydantic.fields import (
    SHAPE_FROZENSET,
    SHAPE_LIST,
    SHAPE_SEQUENCE,
    SHAPE_MAPPING,
    SHAPE_SET,
    SHAPE_SINGLETON,
    SHAPE_TUPLE,
    SHAPE_TUPLE_ELLIPSIS,
    FieldInfo,
    ModelField,
    Required,
    Undefined,
)
from pydantic.schema import get_annotation_from_field_info
from pydantic.typing import evaluate_forwardref, get_args, get_origin
from pydantic.utils import lenient_issubclass
from starlette.background import BackgroundTasks
from starlette.concurrency import run_in_threadpool
from starlette.datastructures import FormData, Headers, QueryParams, UploadFile
from starlette.requests import HTTPConnection, Request
from starlette.responses import Response
from starlette.websockets import WebSocket
from typing_extensions import Annotated

sequence_shapes = {
    SHAPE_LIST,
    SHAPE_SET,
    SHAPE_FROZENSET,
    SHAPE_TUPLE,
    SHAPE_SEQUENCE,
    SHAPE_TUPLE_ELLIPSIS,
}
sequence_types = (list, set, tuple)
sequence_shape_to_type = {
    SHAPE_LIST: list,
    SHAPE_SET: set,
    SHAPE_TUPLE: tuple,
    SHAPE_SEQUENCE: list,
    SHAPE_TUPLE_ELLIPSIS: list,
}

mapping_shapes = {SHAPE_MAPPING}
mapping_types = Mapping
mapping_shapes_to_type = {SHAPE_MAPPING: Mapping}

multipart_not_installed_error = (
    'Form data requires "python-multipart" to be installed. \n'
    'You can install "python-multipart" with: \n\n'
    "pip install python-multipart\n"
)
multipart_incorrect_install_error = (
    'Form data requires "python-multipart" to be installed. '
    'It seems you installed "multipart" instead. \n'
    'You can remove "multipart" with: \n\n'
    "pip uninstall multipart\n\n"
    'And then install "python-multipart" with: \n\n'
    "pip install python-multipart\n"
)


def check_file_field(field: ModelField) -> None:
    field_info = field.field_info
    if isinstance(field_info, params.Form):
        try:
            # __version__ is available in both multiparts, and can be mocked
            from multipart import __version__  # type: ignore

            assert __version__
            try:
                # parse_options_header is only available in the right multipart
                from multipart.multipart import parse_options_header  # type: ignore

                assert parse_options_header
            except ImportError:
                logger.error(multipart_incorrect_install_error)
                raise RuntimeError(multipart_incorrect_install_error) from None
        except ImportError:
            logger.error(multipart_not_installed_error)
            raise RuntimeError(multipart_not_installed_error) from None


def get_param_sub_dependant(
    *,
    param_name: str,
    depends: params.Depends,
    path: str,
    security_scopes: Optional[List[str]] = None,
) -> Dependant:
    assert depends.dependency
    return get_sub_dependant(
        depends=depends,
        dependency=depends.dependency,
        path=path,
        name=param_name,
        security_scopes=security_scopes,
    )


def get_parameterless_sub_dependant(*, depends: params.Depends, path: str) -> Dependant:
    assert callable(
        depends.dependency
    ), "A parameter-less dependency must have a callable dependency"
    return get_sub_dependant(depends=depends, dependency=depends.dependency, path=path)


def get_sub_dependant(
    *,
    depends: params.Depends,
    dependency: Callable[..., Any],
    path: str,
    name: Optional[str] = None,
    security_scopes: Optional[List[str]] = None,
) -> Dependant:
    security_requirement = None
    security_scopes = security_scopes or []
    if isinstance(depends, params.Security):
        dependency_scopes = depends.scopes
        security_scopes.extend(dependency_scopes)
    if isinstance(dependency, SecurityBase):
        use_scopes: List[str] = []
        if isinstance(dependency, (OAuth2, OpenIdConnect)):
            use_scopes = security_scopes
        security_requirement = SecurityRequirement(
            security_scheme=dependency, scopes=use_scopes
        )
    sub_dependant = get_dependant(
        path=path,
        call=dependency,
        name=name,
        security_scopes=security_scopes,
        use_cache=depends.use_cache,
    )
    if security_requirement:
        sub_dependant.security_requirements.append(security_requirement)
    return sub_dependant


CacheKey = Tuple[Optional[Callable[..., Any]], Tuple[str, ...]]


def get_flat_dependant(
    dependant: Dependant,
    *,
    skip_repeats: bool = False,
    visited: Optional[List[CacheKey]] = None,
) -> Dependant:
    if visited is None:
        visited = []
    visited.append(dependant.cache_key)

    flat_dependant = Dependant(
        path_params=dependant.path_params.copy(),
        query_params=dependant.query_params.copy(),
        header_params=dependant.header_params.copy(),
        cookie_params=dependant.cookie_params.copy(),
        body_params=dependant.body_params.copy(),
        security_schemes=dependant.security_requirements.copy(),
        use_cache=dependant.use_cache,
        path=dependant.path,
    )
    for sub_dependant in dependant.dependencies:
        if skip_repeats and sub_dependant.cache_key in visited:
            continue
        flat_sub = get_flat_dependant(
            sub_dependant, skip_repeats=skip_repeats, visited=visited
        )
        flat_dependant.path_params.extend(flat_sub.path_params)
        flat_dependant.query_params.extend(flat_sub.query_params)
        flat_dependant.header_params.extend(flat_sub.header_params)
        flat_dependant.cookie_params.extend(flat_sub.cookie_params)
        flat_dependant.body_params.extend(flat_sub.body_params)
        flat_dependant.security_requirements.extend(flat_sub.security_requirements)
    return flat_dependant


def get_flat_params(dependant: Dependant) -> List[ModelField]:
    flat_dependant = get_flat_dependant(dependant, skip_repeats=True)
    return (
        flat_dependant.path_params
        + flat_dependant.query_params
        + flat_dependant.header_params
        + flat_dependant.cookie_params
    )


def is_scalar_field(field: ModelField) -> bool:
    field_info = field.field_info
    if not (
        field.shape == SHAPE_SINGLETON
        and not lenient_issubclass(field.type_, BaseModel)
        and not lenient_issubclass(field.type_, sequence_types + (dict,))
        and not dataclasses.is_dataclass(field.type_)
        and not isinstance(field_info, params.Body)
    ):
        return False
    if field.sub_fields:
        if not all(is_scalar_field(f) for f in field.sub_fields):
            return False
    return True


def is_scalar_sequence_field(field: ModelField) -> bool:
    if (field.shape in sequence_shapes) and not lenient_issubclass(
        field.type_, BaseModel
    ):
        if field.sub_fields is not None:
            for sub_field in field.sub_fields:
                if not is_scalar_field(sub_field):
                    return False
        return True
    if lenient_issubclass(field.type_, sequence_types):
        return True
    return False

def is_scalar_mapping_field(field: ModelField) -> bool:
    if (field.shape in mapping_shapes) and not lenient_issubclass(
        field.type_, BaseModel
    ):
        if field.sub_fields is None:
            return False
        for sub_field in field.sub_fields:
            if not is_scalar_field(sub_field):
                return False
        return True
    return False


def is_scalar_sequence_mapping_field(field: ModelField) -> bool:
    if (field.shape in mapping_shapes) and not lenient_issubclass(
        field.type_, BaseModel
    ):
        if field.sub_fields is None:
            return False
        for sub_field in field.sub_fields:
            if not is_scalar_sequence_field(sub_field):
                return False
        return True
    return False

def get_typed_signature(call: Callable[..., Any]) -> inspect.Signature:
    signature = inspect.signature(call)
    globalns = getattr(call, "__globals__", {})
    typed_params = [
        inspect.Parameter(
            name=param.name,
            kind=param.kind,
            default=param.default,
            annotation=get_typed_annotation(param.annotation, globalns),
        )
        for param in signature.parameters.values()
    ]
    typed_signature = inspect.Signature(typed_params)
    return typed_signature


def get_typed_annotation(annotation: Any, globalns: Dict[str, Any]) -> Any:
    if isinstance(annotation, str):
        annotation = ForwardRef(annotation)
        annotation = evaluate_forwardref(annotation, globalns, globalns)
    return annotation


def get_typed_return_annotation(call: Callable[..., Any]) -> Any:
    signature = inspect.signature(call)
    annotation = signature.return_annotation

    if annotation is inspect.Signature.empty:
        return None

    globalns = getattr(call, "__globals__", {})
    return get_typed_annotation(annotation, globalns)


def get_dependant(
    *,
    path: str,
    call: Callable[..., Any],
    name: Optional[str] = None,
    security_scopes: Optional[List[str]] = None,
    use_cache: bool = True,
) -> Dependant:
    path_param_names = get_path_param_names(path)
    endpoint_signature = get_typed_signature(call)
    signature_params = endpoint_signature.parameters
    dependant = Dependant(
        call=call,
        name=name,
        path=path,
        security_scopes=security_scopes,
        use_cache=use_cache,
    )
    for param_name, param in signature_params.items():
        is_path_param = param_name in path_param_names
        type_annotation, depends, param_field = analyze_param(
            param_name=param_name,
            annotation=param.annotation,
            value=param.default,
            is_path_param=is_path_param,
        )
        if depends is not None:
            sub_dependant = get_param_sub_dependant(
                param_name=param_name,
                depends=depends,
                path=path,
                security_scopes=security_scopes,
            )
            dependant.dependencies.append(sub_dependant)
            continue
        if add_non_field_param_to_dependency(
            param_name=param_name,
            type_annotation=type_annotation,
            dependant=dependant,
        ):
            assert (
                param_field is None
            ), f"Cannot specify multiple FastAPI annotations for {param_name!r}"
            continue
        assert param_field is not None
        if is_body_param(param_field=param_field, is_path_param=is_path_param):
            dependant.body_params.append(param_field)
        else:
            add_param_to_fields(field=param_field, dependant=dependant)
    return dependant


def add_non_field_param_to_dependency(
    *, param_name: str, type_annotation: Any, dependant: Dependant
) -> Optional[bool]:
    if lenient_issubclass(type_annotation, Request):
        dependant.request_param_name = param_name
        return True
    elif lenient_issubclass(type_annotation, WebSocket):
        dependant.websocket_param_name = param_name
        return True
    elif lenient_issubclass(type_annotation, HTTPConnection):
        dependant.http_connection_param_name = param_name
        return True
    elif lenient_issubclass(type_annotation, Response):
        dependant.response_param_name = param_name
        return True
    elif lenient_issubclass(type_annotation, BackgroundTasks):
        dependant.background_tasks_param_name = param_name
        return True
    elif lenient_issubclass(type_annotation, SecurityScopes):
        dependant.security_scopes_param_name = param_name
        return True
    return None


def analyze_param(
    *,
    param_name: str,
    annotation: Any,
    value: Any,
    is_path_param: bool,
) -> Tuple[Any, Optional[params.Depends], Optional[ModelField]]:
    field_info = None
    used_default_field_info = False
    depends = None
    type_annotation: Any = Any
    if (
        annotation is not inspect.Signature.empty
        and get_origin(annotation) is Annotated  # type: ignore[comparison-overlap]
    ):
        annotated_args = get_args(annotation)
        type_annotation = annotated_args[0]
        fastapi_annotations = [
            arg
            for arg in annotated_args[1:]
            if isinstance(arg, (FieldInfo, params.Depends))
        ]
        assert (
            len(fastapi_annotations) <= 1
        ), f"Cannot specify multiple `Annotated` FastAPI arguments for {param_name!r}"
        fastapi_annotation = next(iter(fastapi_annotations), None)
        if isinstance(fastapi_annotation, FieldInfo):
            # Copy `field_info` because we mutate `field_info.default` below.
            field_info = copy(fastapi_annotation)
            assert field_info.default is Undefined or field_info.default is Required, (
                f"`{field_info.__class__.__name__}` default value cannot be set in"
                f" `Annotated` for {param_name!r}. Set the default value with `=` instead."
            )
            if value is not inspect.Signature.empty:
                assert not is_path_param, "Path parameters cannot have default values"
                field_info.default = value
            else:
                field_info.default = Required
        elif isinstance(fastapi_annotation, params.Depends):
            depends = fastapi_annotation
    elif annotation is not inspect.Signature.empty:
        type_annotation = annotation

    if isinstance(value, params.Depends):
        assert depends is None, (
            "Cannot specify `Depends` in `Annotated` and default value"
            f" together for {param_name!r}"
        )
        assert field_info is None, (
            "Cannot specify a FastAPI annotation in `Annotated` and `Depends` as a"
            f" default value together for {param_name!r}"
        )
        depends = value
    elif isinstance(value, FieldInfo):
        assert field_info is None, (
            "Cannot specify FastAPI annotations in `Annotated` and default value"
            f" together for {param_name!r}"
        )
        field_info = value

    if depends is not None and depends.dependency is None:
        depends.dependency = type_annotation

    if lenient_issubclass(
        type_annotation,
        (Request, WebSocket, HTTPConnection, Response, BackgroundTasks, SecurityScopes),
    ):
        assert depends is None, f"Cannot specify `Depends` for type {type_annotation!r}"
        assert (
            field_info is None
        ), f"Cannot specify FastAPI annotation for type {type_annotation!r}"
    elif field_info is None and depends is None:
        default_value = value if value is not inspect.Signature.empty else Required
        if is_path_param:
            # We might check here that `default_value is Required`, but the fact is that the same
            # parameter might sometimes be a path parameter and sometimes not. See
            # `tests/test_infer_param_optionality.py` for an example.
            field_info = params.Path()
        else:
            field_info = params.Query(default=default_value)
        used_default_field_info = True

    field = None
    if field_info is not None:
        if is_path_param:
            assert isinstance(field_info, params.Path), (
                f"Cannot use `{field_info.__class__.__name__}` for path param"
                f" {param_name!r}"
            )
        elif (
            isinstance(field_info, params.Param)
            and getattr(field_info, "in_", None) is None
        ):
            field_info.in_ = params.ParamTypes.query
        annotation = get_annotation_from_field_info(
            annotation if annotation is not inspect.Signature.empty else Any,
            field_info,
            param_name,
        )
        if not field_info.alias and getattr(field_info, "convert_underscores", None):
            alias = param_name.replace("_", "-")
        else:
            alias = field_info.alias or param_name
        field = create_response_field(
            name=param_name,
            type_=annotation,
            default=field_info.default,
            alias=alias,
            required=field_info.default in (Required, Undefined),
            field_info=field_info,
        )
        if used_default_field_info:
            if lenient_issubclass(field.type_, UploadFile):
                field.field_info = params.File(field_info.default)
            elif not is_scalar_field(field=field):
                field.field_info = params.Body(field_info.default)

    return type_annotation, depends, field


def is_body_param(*, param_field: ModelField, is_path_param: bool) -> bool:
    if is_path_param:
        assert is_scalar_field(
            field=param_field
        ), "Path params must be of one of the supported types"
        return False
    elif is_scalar_field(field=param_field):
        return False
    elif isinstance(
        param_field.field_info, (params.Query, params.Header)
    ) and is_scalar_sequence_field(param_field):
        return False
    elif isinstance(
        param_field.field_info, (params.Query, params.Header)
    ) and (is_scalar_sequence_mapping_field(param_field) or is_scalar_mapping_field(param_field)):
        return False
    else:
        assert isinstance(
            param_field.field_info, params.Body
        ), f"Param: {param_field.name} can only be a request body, using Body()"
        return True


def add_param_to_fields(*, field: ModelField, dependant: Dependant) -> None:
    field_info = cast(params.Param, field.field_info)
    if field_info.in_ == params.ParamTypes.path:
        dependant.path_params.append(field)
    elif field_info.in_ == params.ParamTypes.query:
        dependant.query_params.append(field)
    elif field_info.in_ == params.ParamTypes.header:
        dependant.header_params.append(field)
    else:
        assert (
            field_info.in_ == params.ParamTypes.cookie
        ), f"non-body parameters must be in path, query, header or cookie: {field.name}"
        dependant.cookie_params.append(field)


def is_coroutine_callable(call: Callable[..., Any]) -> bool:
    if inspect.isroutine(call):
        return inspect.iscoroutinefunction(call)
    if inspect.isclass(call):
        return False
    dunder_call = getattr(call, "__call__", None)  # noqa: B004
    return inspect.iscoroutinefunction(dunder_call)


def is_async_gen_callable(call: Callable[..., Any]) -> bool:
    if inspect.isasyncgenfunction(call):
        return True
    dunder_call = getattr(call, "__call__", None)  # noqa: B004
    return inspect.isasyncgenfunction(dunder_call)


def is_gen_callable(call: Callable[..., Any]) -> bool:
    if inspect.isgeneratorfunction(call):
        return True
    dunder_call = getattr(call, "__call__", None)  # noqa: B004
    return inspect.isgeneratorfunction(dunder_call)


async def solve_generator(
    *, call: Callable[..., Any], stack: AsyncExitStack, sub_values: Dict[str, Any]
) -> Any:
    if is_gen_callable(call):
        cm = contextmanager_in_threadpool(contextmanager(call)(**sub_values))
    elif is_async_gen_callable(call):
        cm = asynccontextmanager(call)(**sub_values)
    return await stack.enter_async_context(cm)


async def solve_dependencies(
    *,
    request: Union[Request, WebSocket],
    dependant: Dependant,
    body: Optional[Union[Dict[str, Any], FormData]] = None,
    background_tasks: Optional[BackgroundTasks] = None,
    response: Optional[Response] = None,
    dependency_overrides_provider: Optional[Any] = None,
    dependency_cache: Optional[Dict[Tuple[Callable[..., Any], Tuple[str]], Any]] = None,
) -> Tuple[
    Dict[str, Any],
    List[ErrorWrapper],
    Optional[BackgroundTasks],
    Response,
    Dict[Tuple[Callable[..., Any], Tuple[str]], Any],
]:
    values: Dict[str, Any] = {}
    errors: List[ErrorWrapper] = []
    if response is None:
        response = Response()
        del response.headers["content-length"]
        response.status_code = None  # type: ignore
    dependency_cache = dependency_cache or {}
    sub_dependant: Dependant
    for sub_dependant in dependant.dependencies:
        sub_dependant.call = cast(Callable[..., Any], sub_dependant.call)
        sub_dependant.cache_key = cast(
            Tuple[Callable[..., Any], Tuple[str]], sub_dependant.cache_key
        )
        call = sub_dependant.call
        use_sub_dependant = sub_dependant
        if (
            dependency_overrides_provider
            and dependency_overrides_provider.dependency_overrides
        ):
            original_call = sub_dependant.call
            call = getattr(
                dependency_overrides_provider, "dependency_overrides", {}
            ).get(original_call, original_call)
            use_path: str = sub_dependant.path  # type: ignore
            use_sub_dependant = get_dependant(
                path=use_path,
                call=call,
                name=sub_dependant.name,
                security_scopes=sub_dependant.security_scopes,
            )

        solved_result = await solve_dependencies(
            request=request,
            dependant=use_sub_dependant,
            body=body,
            background_tasks=background_tasks,
            response=response,
            dependency_overrides_provider=dependency_overrides_provider,
            dependency_cache=dependency_cache,
        )
        (
            sub_values,
            sub_errors,
            background_tasks,
            _,  # the subdependency returns the same response we have
            sub_dependency_cache,
        ) = solved_result
        dependency_cache.update(sub_dependency_cache)
        if sub_errors:
            errors.extend(sub_errors)
            continue
        if sub_dependant.use_cache and sub_dependant.cache_key in dependency_cache:
            solved = dependency_cache[sub_dependant.cache_key]
        elif is_gen_callable(call) or is_async_gen_callable(call):
            stack = request.scope.get("fastapi_astack")
            assert isinstance(stack, AsyncExitStack)
            solved = await solve_generator(
                call=call, stack=stack, sub_values=sub_values
            )
        elif is_coroutine_callable(call):
            solved = await call(**sub_values)
        else:
            solved = await run_in_threadpool(call, **sub_values)
        if sub_dependant.name is not None:
            values[sub_dependant.name] = solved
        if sub_dependant.cache_key not in dependency_cache:
            dependency_cache[sub_dependant.cache_key] = solved
    path_values, path_errors = request_params_to_args(
        dependant.path_params, request.path_params
    )
    query_values, query_errors = request_params_to_args(
        dependant.query_params, request.query_params
    )
    header_values, header_errors = request_params_to_args(
        dependant.header_params, request.headers
    )
    cookie_values, cookie_errors = request_params_to_args(
        dependant.cookie_params, request.cookies
    )
    values.update(path_values)
    values.update(query_values)
    values.update(header_values)
    values.update(cookie_values)
    errors += path_errors + query_errors + header_errors + cookie_errors
    if dependant.body_params:
        (
            body_values,
            body_errors,
        ) = await request_body_to_args(  # body_params checked above
            required_params=dependant.body_params, received_body=body
        )
        values.update(body_values)
        errors.extend(body_errors)
    if dependant.http_connection_param_name:
        values[dependant.http_connection_param_name] = request
    if dependant.request_param_name and isinstance(request, Request):
        values[dependant.request_param_name] = request
    elif dependant.websocket_param_name and isinstance(request, WebSocket):
        values[dependant.websocket_param_name] = request
    if dependant.background_tasks_param_name:
        if background_tasks is None:
            background_tasks = BackgroundTasks()
        values[dependant.background_tasks_param_name] = background_tasks
    if dependant.response_param_name:
        values[dependant.response_param_name] = response
    if dependant.security_scopes_param_name:
        values[dependant.security_scopes_param_name] = SecurityScopes(
            scopes=dependant.security_scopes
        )
    return values, errors, background_tasks, response, dependency_cache


def request_params_to_args(
    required_params: Sequence[ModelField],
    received_params: Union[Mapping[str, Any], QueryParams, Headers],
) -> Tuple[Dict[str, Any], List[ErrorWrapper]]:
    values = {}
    errors = []
    for field in required_params:
        if is_scalar_sequence_field(field) and isinstance(
            received_params, (QueryParams, Headers)
        ):
            value = received_params.getlist(field.alias) or field.default
        else:
            value = received_params.get(field.alias)
        field_info = field.field_info
        assert isinstance(
            field_info, params.Param
        ), "Params must be subclasses of Param"
        if value is None:
            if field.required:
                errors.append(
                    ErrorWrapper(
                        MissingError(), loc=(field_info.in_.value, field.alias)
                    )
                )
            else:
                values[field.name] = deepcopy(field.default)
            continue
        v_, errors_ = field.validate(
            value, values, loc=(field_info.in_.value, field.alias)
        )
        if isinstance(errors_, ErrorWrapper):
            errors.append(errors_)
        elif isinstance(errors_, list):
            errors.extend(errors_)
        else:
            values[field.name] = v_
    return values, errors


async def request_body_to_args(
    required_params: List[ModelField],
    received_body: Optional[Union[Dict[str, Any], FormData]],
) -> Tuple[Dict[str, Any], List[ErrorWrapper]]:
    values = {}
    errors = []
    if required_params:
        field = required_params[0]
        field_info = field.field_info
        embed = getattr(field_info, "embed", None)
        field_alias_omitted = len(required_params) == 1 and not embed
        if field_alias_omitted:
            received_body = {field.alias: received_body}

        for field in required_params:
            loc: Tuple[str, ...]
            if field_alias_omitted:
                loc = ("body",)
            else:
                loc = ("body", field.alias)

            value: Optional[Any] = None
            if received_body is not None:
                if (
                    field.shape in sequence_shapes or field.type_ in sequence_types
                ) and isinstance(received_body, FormData):
                    value = received_body.getlist(field.alias)
                else:
                    try:
                        value = received_body.get(field.alias)
                    except AttributeError:
                        errors.append(get_missing_field_error(loc))
                        continue
            if (
                value is None
                or (isinstance(field_info, params.Form) and value == "")
                or (
                    isinstance(field_info, params.Form)
                    and field.shape in sequence_shapes
                    and len(value) == 0
                )
            ):
                if field.required:
                    errors.append(get_missing_field_error(loc))
                else:
                    values[field.name] = deepcopy(field.default)
                continue
            if (
                isinstance(field_info, params.File)
                and lenient_issubclass(field.type_, bytes)
                and isinstance(value, UploadFile)
            ):
                value = await value.read()
            elif (
                field.shape in sequence_shapes
                and isinstance(field_info, params.File)
                and lenient_issubclass(field.type_, bytes)
                and isinstance(value, sequence_types)
            ):
                results: List[Union[bytes, str]] = []

                async def process_fn(
                    fn: Callable[[], Coroutine[Any, Any, Any]]
                ) -> None:
                    result = await fn()
                    results.append(result)  # noqa: B023

                async with anyio.create_task_group() as tg:
                    for sub_value in value:
                        tg.start_soon(process_fn, sub_value.read)
                value = sequence_shape_to_type[field.shape](results)

            v_, errors_ = field.validate(value, values, loc=loc)

            if isinstance(errors_, ErrorWrapper):
                errors.append(errors_)
            elif isinstance(errors_, list):
                errors.extend(errors_)
            else:
                values[field.name] = v_
    return values, errors


def get_missing_field_error(loc: Tuple[str, ...]) -> ErrorWrapper:
    missing_field_error = ErrorWrapper(MissingError(), loc=loc)
    return missing_field_error


def get_body_field(*, dependant: Dependant, name: str) -> Optional[ModelField]:
    flat_dependant = get_flat_dependant(dependant)
    if not flat_dependant.body_params:
        return None
    first_param = flat_dependant.body_params[0]
    field_info = first_param.field_info
    embed = getattr(field_info, "embed", None)
    body_param_names_set = {param.name for param in flat_dependant.body_params}
    if len(body_param_names_set) == 1 and not embed:
        check_file_field(first_param)
        return first_param
    # If one field requires to embed, all have to be embedded
    # in case a sub-dependency is evaluated with a single unique body field
    # That is combined (embedded) with other body fields
    for param in flat_dependant.body_params:
        setattr(param.field_info, "embed", True)  # noqa: B010
    model_name = "Body_" + name
    BodyModel: Type[BaseModel] = create_model(model_name)
    for f in flat_dependant.body_params:
        BodyModel.__fields__[f.name] = f
    required = any(True for f in flat_dependant.body_params if f.required)

    BodyFieldInfo_kwargs: Dict[str, Any] = {"default": None}
    if any(isinstance(f.field_info, params.File) for f in flat_dependant.body_params):
        BodyFieldInfo: Type[params.Body] = params.File
    elif any(isinstance(f.field_info, params.Form) for f in flat_dependant.body_params):
        BodyFieldInfo = params.Form
    else:
        BodyFieldInfo = params.Body

        body_param_media_types = [
            f.field_info.media_type
            for f in flat_dependant.body_params
            if isinstance(f.field_info, params.Body)
        ]
        if len(set(body_param_media_types)) == 1:
            BodyFieldInfo_kwargs["media_type"] = body_param_media_types[0]
    final_field = create_response_field(
        name="body",
        type_=BodyModel,
        required=required,
        alias="body",
        field_info=BodyFieldInfo(**BodyFieldInfo_kwargs),
    )
    check_file_field(final_field)
    return final_field
