from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TypeVar, Generic

from src.domain.events.base import BaseEvent


ET = TypeVar('ET', bound=BaseEvent)
RT = TypeVar('RT')


@dataclass(frozen=True)
class BaseEventHandler(ABC, Generic[ET, RT]):
    @abstractmethod
    async def handle(self, event: ET) -> RT:
        ...
        