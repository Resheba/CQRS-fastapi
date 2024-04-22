from dataclasses import dataclass

from src.domain.queries.base import BaseQuery


@dataclass(frozen=True, eq=False)
class GetMessageQuery(BaseQuery):
    id: str | None = None
    message: str | None = None
    user_id: str | None = None
