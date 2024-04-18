from abc import ABC
from datetime import datetime
from uuid import UUID, uuid4
from dataclasses import dataclass, field


@dataclass(frozen=True)
class BaseEvent(ABC):
    id: UUID = field(default_factory=uuid4, kw_only=True)
    created_at: datetime = field(default_factory=datetime.now, kw_only=True)
