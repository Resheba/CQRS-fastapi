from dataclasses import dataclass

from src.domain.entities.user import User
from src.infrastructure.repository.base.memory import BaseMemoryRepository


@dataclass(eq=False)
class UserMemoryRepository(BaseMemoryRepository[User]):
    pass
