from typing import Iterable
from sqlalchemy.orm import DeclarativeBase
from pydantic import BaseModel


class Serializer:
    @staticmethod
    def from_sqlalchemy(_from: DeclarativeBase | Iterable[DeclarativeBase], _to: type[BaseModel], /) -> tuple[BaseModel] | BaseModel | None:
        if _from is None:
            return None
        if isinstance(_from, Iterable):
            return tuple(_to.model_validate(f, from_attributes=True) for f in _from)
        return _to.model_validate(_from, from_attributes=True)
    