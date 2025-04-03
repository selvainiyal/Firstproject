import importlib

import pytest
from dirty_equals import IsDict
from fastapi.testclient import TestClient
from inline_snapshot import snapshot

from tests.utils import needs_py39, needs_py310


@pytest.fixture(
    name="client",
    params=[
        "tutorial001",
        pytest.param("tutorial001_py39", marks=needs_py39),
        pytest.param("tutorial001_py310", marks=needs_py310),
        "tutorial001_an",
        pytest.param("tutorial001_an_py39", marks=needs_py39),
        pytest.param("tutorial001_an_py310", marks=needs_py310),
    ],
)
def get_client(request: pytest.FixtureRequest):
    mod = importlib.import_module(f"docs_src.header_param_models.{request.param}")

    client = TestClient(mod.app)
    return client


def test_header_param_model(client: TestClient):
    response = client.get(
        "/items/",
        headers=[
            ("save-data", "true"),
            ("if-modified-since", "yesterday"),
            ("traceparent", "123"),
            ("x-tag", "one"),
            ("x-tag", "two"),
        ],
    )
    assert response.status_code == 200
    assert response.json() == {
        "host": "testserver",
        "save_data": True,
        "if_modified_since": "yesterday",
        "traceparent": "123",
        "x_tag": ["one", "two"],
    }


def test_header_param_model_defaults(client: TestClient):
    response = client.get("/items/", headers=[("save-data", "true")])
    assert response.status_code == 200
    assert response.json() == {
        "host": "testserver",
        "save_data": True,
        "if_modified_since": None,
        "traceparent": None,
        "x_tag": [],
    }


def test_header_param_model_invalid(client: TestClient):
    response = client.get("/items/")
    assert response.status_code == 422
    assert response.json() == snapshot(
        {
            "detail": [
                IsDict(
                    {
                        "type": "missing",
                        "loc": ["header", "save_data"],
                        "msg": "Field required",
                        "input": {
                            "x_tag": [],
                            "host": "testserver",
                            "accept": "*/*",
                            "accept-encoding": "gzip, deflate",
                            "connection": "keep-alive",
                            "user-agent": "testclient",
                            "if_modified_since": None,
                            "traceparent": None,
                        },
                    }
                )
                | IsDict(
                    # TODO: remove when deprecating Pydantic v1
                    {
                        "type": "value_error.missing",
                        "loc": ["header", "save_data"],
                        "msg": "field required",
                    }
                )
            ]
        }
    )


def test_header_param_model_extra(client: TestClient):
    response = client.get(
        "/items/", headers=[("save-data", "true"), ("tool", "plumbus")]
    )
    assert response.status_code == 200, response.text
    assert response.json() == snapshot(
        {
            "host": "testserver",
            "save_data": True,
            "if_modified_since": None,
            "traceparent": None,
            "x_tag": [],
        }
    )


def test_openapi_schema(client: TestClient):
    response = client.get("/openapi.json")
    assert response.status_code == 200, response.text
    assert response.json() == snapshot(
        {
            "openapi": "3.1.0",
            "info": {"title": "FastAPI", "version": "0.1.0"},
            "paths": {
                "/items/": {
                    "get": {
                        "summary": "Read Items",
                        "operationId": "read_items_items__get",
                        "parameters": [
                            {
                                "name": "host",
                                "in": "header",
                                "required": True,
                                "schema": {"type": "string", "title": "Host"},
                            },
                            {
                                "name": "save-data",
                                "in": "header",
                                "required": True,
                                "schema": {"type": "boolean", "title": "Save Data"},
                            },
                            {
                                "name": "if-modified-since",
                                "in": "header",
                                "required": False,
                                "schema": IsDict(
                                    {
                                        "anyOf": [{"type": "string"}, {"type": "null"}],
                                        "title": "If Modified Since",
                                    }
                                )
                                | IsDict(
                                    # TODO: remove when deprecating Pydantic v1
                                    {
                                        "type": "string",
                                        "title": "If Modified Since",
                                    }
                                ),
                            },
                            {
                                "name": "traceparent",
                                "in": "header",
                                "required": False,
                                "schema": IsDict(
                                    {
                                        "anyOf": [{"type": "string"}, {"type": "null"}],
                                        "title": "Traceparent",
                                    }
                                )
                                | IsDict(
                                    # TODO: remove when deprecating Pydantic v1
                                    {
                                        "type": "string",
                                        "title": "Traceparent",
                                    }
                                ),
                            },
                            {
                                "name": "x-tag",
                                "in": "header",
                                "required": False,
                                "schema": {
                                    "type": "array",
                                    "items": {"type": "string"},
                                    "default": [],
                                    "title": "X Tag",
                                },
                            },
                        ],
                        "responses": {
                            "200": {
                                "description": "Successful Response",
                                "content": {"application/json": {"schema": {}}},
                            },
                            "422": {
                                "description": "Validation Error",
                                "content": {
                                    "application/json": {
                                        "schema": {
                                            "$ref": "#/components/schemas/HTTPValidationError"
                                        }
                                    }
                                },
                            },
                        },
                    }
                }
            },
            "components": {
                "schemas": {
                    "HTTPValidationError": {
                        "properties": {
                            "detail": {
                                "items": {
                                    "$ref": "#/components/schemas/ValidationError"
                                },
                                "type": "array",
                                "title": "Detail",
                            }
                        },
                        "type": "object",
                        "title": "HTTPValidationError",
                    },
                    "ValidationError": {
                        "properties": {
                            "loc": {
                                "items": {
                                    "anyOf": [{"type": "string"}, {"type": "integer"}]
                                },
                                "type": "array",
                                "title": "Location",
                            },
                            "msg": {"type": "string", "title": "Message"},
                            "type": {"type": "string", "title": "Error Type"},
                        },
                        "type": "object",
                        "required": ["loc", "msg", "type"],
                        "title": "ValidationError",
                    },
                }
            },
        }
    )
