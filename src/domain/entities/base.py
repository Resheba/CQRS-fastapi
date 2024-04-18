from abc import ABC
from uuid import UUID, uuid4
from dataclasses import dataclass, field


@dataclass
class BaseEntity(ABC):
    id: UUID = field(default_factory=uuid4, kw_only=True)
