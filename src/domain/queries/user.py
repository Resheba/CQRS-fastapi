from dataclasses import dataclass

from src.domain.queries.base import BaseQuery


@dataclass(frozen=True, eq=False)
class GetUserQuery(BaseQuery):
    user_id: str | None = None
    username: str | None = None
