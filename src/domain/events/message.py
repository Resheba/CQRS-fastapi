from dataclasses import dataclass

from src.domain.entities.message import Message
from src.domain.events.base import BaseEvent


@dataclass(frozen=True)
class MessageSent(BaseEvent):
    message: Message
