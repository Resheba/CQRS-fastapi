from typing import Iterable, Mapping, Generic, TypeVar
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel

from src.infrastructure.repository.base.base import BaseRepository
from src.infrastructure.repository.base.serializer import Serializer


MT = TypeVar('MT', bound=DeclarativeBase)
RT = TypeVar('RT', bound=BaseModel)


class BaseSQLAlchemyRepository(BaseRepository, Generic[MT, RT]):
    orm_model: type[MT]
    dto: type[RT]

    def __init__(self, session: AsyncSession) -> None:
        self.session: AsyncSession = session

    def add(self, data: Mapping | Iterable[Mapping], *, autocommit: bool = True) -> RT:
        if isinstance(data, Iterable):
            orm: list[MT] = [self.orm_model(**d) for d in data]
        else:
            orm: MT = [self.orm_model(**data)]
        self.session.add_all(orm)
        if autocommit:
            self.session.commit()
        return Serializer.from_sqlalchemy(orm, self.dto)
    
    def get():
        pass

    def delete():
        pass

    def update():
        pass
