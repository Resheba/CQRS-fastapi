from dataclasses import dataclass

from src.domain.entities.message import Message
from src.infrastructure.repository.base.memory import BaseMemoryRepository


@dataclass(eq=False)
class MessageMemoryRepository(BaseMemoryRepository[Message]):
    pass

