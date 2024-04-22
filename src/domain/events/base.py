from abc import ABC
from datetime import datetime
from uuid import uuid4
from dataclasses import dataclass, field


@dataclass(frozen=True)
class BaseEvent(ABC):
    id: str = field(default_factory=lambda: uuid4().__str__(), kw_only=True)
    created_at: datetime = field(default_factory=datetime.now, kw_only=True)
