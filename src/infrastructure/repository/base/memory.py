from typing import Any
from src.infrastructure.repository.base.base import BaseRepository


class BaseMemoryRepository(BaseRepository):
    storage: list[dict] = list()

    @classmethod
    async def get(cls, **filters):
        return cls.storage
    
    @classmethod
    async def add(cls, data: dict):
        cls.storage.append(data)

    @classmethod
    async def delete(cls, id: Any):
        cls.storage = [i for i in cls.storage if i.get('id') != id]

    @classmethod
    async def update(cls):
        ...
