from pydantic import BaseModel
from typing import Literal, Optional, Generic, TypeVar


T = TypeVar('T')


class BaseResponse(BaseModel, Generic[T]):
    status: Literal['success', 'error', 'fail'] = 'success'
    msg: Optional[str] = None
    data: Optional[T] = None
