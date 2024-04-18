from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TypeVar, Generic

from src.domain.commands.base import BaseCommand


CT = TypeVar('CT', bound=BaseCommand)
RT = TypeVar('RT')


@dataclass(frozen=True)
class BaseCommandHandler(ABC, Generic[CT, RT]):
    @abstractmethod
    async def handle(self, command: CT) -> RT:
        ...
        