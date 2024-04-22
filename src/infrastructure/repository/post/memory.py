from dataclasses import dataclass

from src.domain.entities.post import Post
from src.infrastructure.repository.base.memory import BaseMemoryRepository


@dataclass(eq=False)
class PostMemoryRepository(BaseMemoryRepository[Post]):
    pass
