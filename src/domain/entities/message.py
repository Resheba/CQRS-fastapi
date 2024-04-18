from uuid import UUID
from dataclasses import dataclass

from src.domain.entities.base import BaseEntity
from src.domain.descriptors import MessageText 


@dataclass
class Message(BaseEntity):
    message: MessageText
    user: UUID
