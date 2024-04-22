from functools import wraps
from typing import Any, Callable
from fastapi import Request, status
from fastapi.responses import JSONResponse

from src.domain.exceptions.base import DomainException
from src.infrastructure.exceptions.base import InfrastructureException 

from .response import BaseResponse


class BaseHTTPException(Exception):
    def __init__(
            self, 
            status_code: int, 
            msg: str | None = None, 
            data: Any = None
            ) -> None:
        self.status_code = status_code; self.msg = msg; self.data = data

    @staticmethod
    def handler(request: Request, ex: 'BaseHTTPException') -> JSONResponse:
        status: str = 'success'
        if 400 <= ex.status_code < 500:
            status: str = 'error'
        elif ex.status_code >= 500:
            status: str = 'fail'
        return JSONResponse(
            status_code=ex.status_code,
            content=BaseResponse(
                status=status,
                msg=ex.msg,
                data=ex.data
            ).model_dump(exclude_none=True)
        )
    
    @classmethod
    def handle(cls, callable: Callable) -> Any:
        @wraps(callable)
        async def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                return await callable(*args, **kwargs)
            except (DomainException) as ex:
                raise cls(
                    status_code=status.HTTP_409_CONFLICT,
                    msg=ex.message,
                    data=ex.__class__.__name__
                )
            except (InfrastructureException, Exception) as ex:
                raise cls(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    msg=str(ex),
                    data=ex.__class__.__name__
                )
        return wrapper
    