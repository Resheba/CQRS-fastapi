from abc import ABC
from uuid import UUID, uuid4
from dataclasses import dataclass, field


@dataclass
class BaseEntity(ABC):
    id: str = field(default_factory=lambda: str(uuid4()), kw_only=True)
