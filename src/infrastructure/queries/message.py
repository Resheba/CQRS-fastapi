from dataclasses import dataclass
from typing import Tuple

from src.infrastructure.repository.message.base import BaseMessageRepository
from src.infrastructure.queries.base import BaseQueryHandler
from src.domain.entities.message import Message
from src.domain.queries.message import GetMessageQuery


@dataclass(frozen=True, eq=False)
class GetMessageQueryHandler(BaseQueryHandler[GetMessageQuery, Tuple[Message]]):
    repository: BaseMessageRepository

    async def handle(self, query: GetMessageQuery) -> Tuple[Message]:
        result = await self.repository.get(
            id=query.id,
            message=query.message,
            user=query.user_id,
        )
        return tuple(result)
