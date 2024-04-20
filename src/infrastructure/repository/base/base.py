from abc import ABC, abstractmethod


class BaseRepository(ABC):
    @abstractmethod
    async def add():
        ...

    @abstractmethod
    async def get():
        ...

    @abstractmethod
    async def delete():
        ...
    
    @abstractmethod
    async def update():
        ...
