from typing import Any
from src.infrastructure.repository.base.base import BaseRepository


class BaseMemoryRepository(BaseRepository):
    storage: list[Any]

    @classmethod
    def get(cls, **filters):
        return cls.storage
    
    @classmethod
    def add(cls, data: Any):
        cls.storage.append(data)

    @classmethod
    def delete(cls):
        ...

    @classmethod
    def update(cls):
        ...
