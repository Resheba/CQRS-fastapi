from dataclasses import dataclass

from src.domain.entities.user import User
from src.domain.events.base import BaseEvent


@dataclass(frozen=True)
class UserCreated(BaseEvent):
    user: User
