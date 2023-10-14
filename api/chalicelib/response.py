
from typing import Any

from chalice.app import Response
from returns.result import Result, Success, Failure
from returns.pipeline import is_successful
from pydantic import BaseModel, Field

from chalicelib import error

class ResponseModel(BaseModel):
    errors: list[error.Summary] | None = Field(default=None)
    version: int = 1
    data: Any

    class Config:
        json_encoders = {
            list[error.Summary] | None: lambda v: v or None,
        }

def response(result:Success|Failure, *, status_code:int=0) -> Response:
    status_code_from_param = status_code

    resp = ResponseModel(data={})

    if is_successful(result):
        status_code = 200
        resp.data = result.unwrap()
    else:
        status_code = 400
        err = result.failure()

        if isinstance(err, error.Error):
            resp.errors = err.summaries
        else:
            resp.errors = [
                error.Summary(
                    code=error.CODE_UNKNOWN,
                    message='不明なエラーです',
                )
            ]

    if status_code_from_param < 100 or status_code_from_param >= 600:
        status_code = status_code_from_param

    r = Response(
        body=resp.model_dump_json(exclude_none=True),
        status_code=status_code
    )

    return r
