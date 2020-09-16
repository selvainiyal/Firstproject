import itertools
from typing import Any, Dict, Iterable, List, Optional, Type

from pydantic import BaseModel, Field
from starlette.requests import Request


class PaginationParam(object):
    """
    base pagination param
    every page_mode that used have to inherit this class
    """

    page_size = 10
    max_page_size = 100
    min_page_size = 5
    page_size_query_param: str = "page_size"
    page_query_param: str = "page_num"


class Pagination(BaseModel):
    """
    pagination model
    """

    count: int = Field(0, ge=0)
    next: str = Field(None)
    previous: str = Field(None)
    results: list = []


def get_pagination(response_model: Optional[Type[Any]]) -> Optional[Type[Any]]:
    # produce the pagination model

    if response_model is None:
        return Pagination
    elif issubclass(response_model, Pagination):
        return response_model

    class _Pagination(Pagination):
        results: List[response_model] = []  # type: ignore

    return _Pagination


def count(iterable: Any) -> int:
    def _count_iter(_iterable: Any) -> int:
        return len(_iterable)

    """
    if hasattr(iterable, "__len__"):
        return _count_iter(iterable)
    else:
        return 0
    """
    return _count_iter(iterable)


def between(start: int, end: int, iterable: Iterable) -> List:
    # return the object of iterable between start and end

    items = [_item for _item in itertools.islice(iter(iterable), start, end)]
    try:
        return [model_to_dict(_item) for _item in items]
    except Exception:
        return [_item for _item in items]


def model_to_dict(model: Any) -> Dict:
    # trans model type to dict
    def _model_to_dict(_model: Any) -> Iterable:
        for col in _model.__table__.columns:
            yield getattr(_model, col.name), col.name

    return dict((g[1], g[0]) for g in _model_to_dict(model))


def handle_error_struct(data: Any) -> Dict:
    # handle the data format when it's illegal
    try:
        return {"results": [dict(data)], "count": 1, "next": None, "previous": None}
    except TypeError:
        return {"results": [data], "count": 1, "next": None, "previous": None}


def page_split(
    request: Request,
    raw_response: Iterable,
    page_field: Type[PaginationParam] = PaginationParam,
) -> Dict:
    try:
        # get the pagination info
        page_num = int(request.query_params.get(page_field.page_query_param, 1))
        page_size = int(
            request.query_params.get(
                page_field.page_size_query_param, page_field.page_size
            )
        )
    except ValueError:
        raise ValueError(
            f"{page_field.page_query_param} and {page_field.page_size_query_param} requires integer type"
        )
    # check the values
    if (
        page_size > page_field.max_page_size
        or page_size < page_field.min_page_size
        or page_size <= 0
    ):
        raise ValueError(
            f"{page_field.page_size_query_param} should between {page_field.max_page_size} and {page_field.min_page_size} and bigger than 0"
        )
    if page_num <= 0:
        raise ValueError(f"{page_field.page_size_query_param} should bigger than 0!")
    # produce url
    base_url = f"{request.url.scheme}://{request.url.netloc}{request.url.path}"
    query_params = dict(request.query_params.items())
    length = count(raw_response)
    if length == 0:
        return {"results": [], "count": 0, "next": None, "previous": None}
    if page_num == 1:
        previous_url = None
    else:
        query_params[page_field.page_query_param] = page_num - 1
        previous_url = f'{base_url}?{"&".join([f"{key}={value}" for key, value in query_params.items()])}'

    if page_size * page_num >= length:
        next_url = None
    else:
        query_params[page_field.page_query_param] = page_num + 1
        next_url = f'{base_url}?{"&".join([f"{key}={value}" for key, value in query_params.items()])}'
    # format the data
    return {
        "count": length,
        "next": next_url,
        "previous": previous_url,
        "results": between(
            (page_num - 1) * page_size, page_num * page_size, raw_response
        ),
    }
