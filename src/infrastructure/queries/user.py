from dataclasses import dataclass

from src.infrastructure.repository.user.base import BaseUserRepository
from src.infrastructure.queries.base import BaseQueryHandler
from src.domain.entities.user import User
from src.domain.queries.user import GetUserQuery


@dataclass(frozen=True, eq=False)
class GetUserQueryHandler(BaseQueryHandler[GetUserQuery, tuple[User]]):
    repository: BaseUserRepository

    async def handle(self, query: GetUserQuery) -> tuple[User]:
        result = await self.repository.get(id=query.user_id, username=query.username)
        return tuple(result)
