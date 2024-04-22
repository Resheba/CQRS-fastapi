from dataclasses import dataclass

from src.domain.queries.base import BaseQuery


@dataclass(frozen=True, eq=False)
class GetPostQuery(BaseQuery):
    id: str | None = None
    title: str | None = None
    text: str | None = None
    user_id: str | None = None

