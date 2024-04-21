from dataclasses import dataclass

from src.domain.entities.base import BaseEntity
from src.domain.descriptors import MessageText 


@dataclass
class Message(BaseEntity):
    message: MessageText
    user: str

    def dict(self) -> dict:
        return {'id': self.id, 'message': self.message.value, 'user': self.user}