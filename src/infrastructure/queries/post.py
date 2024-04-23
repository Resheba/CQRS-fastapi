from dataclasses import dataclass

from src.infrastructure.repository.post.base import BasePostRepository
from src.infrastructure.queries.base import BaseQueryHandler
from src.domain.entities.post import Post
from src.domain.queries.post import GetPostQuery


@dataclass(frozen=True, eq=False)
class GetPostQueryHandler(BaseQueryHandler[GetPostQuery, tuple[Post]]):
    repository: BasePostRepository

    async def handle(self, query: GetPostQuery) -> tuple[Post]:
        result = await self.repository.get(
            id=query.id,
            title=query.title,
            text=query.text,
            user_id=query.user_id,
        )
        return tuple(result)
