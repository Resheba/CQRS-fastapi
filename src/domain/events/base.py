from abc import ABC
from uuid import UUID, uuid4
from dataclasses import dataclass, field


@dataclass(frozen=True)
class BaseEvent(ABC):
    id: UUID = field(default_factory=uuid4, kw_only=True)
