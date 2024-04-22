from typing import Any, TypeVar, Generic
from dataclasses import dataclass, field

from src.domain.entities.base import BaseEntity
from src.infrastructure.repository.base.base import BaseRepository


ET = TypeVar('ET', bound=BaseEntity)


@dataclass(eq=False)
class BaseMemoryRepository(BaseRepository, Generic[ET]):
    storage: list[ET] = field(default_factory=list, kw_only=True)

    async def get(self, **filters) -> tuple[ET]:
        return self.storage
    
    async def add(self, data: Any) -> ET:
        self.storage.append(data)
        return data

    async def delete(self, id: Any) -> None:
        self.storage = [i for i in self.storage if i.id != id]

    async def update(self):
        ...
