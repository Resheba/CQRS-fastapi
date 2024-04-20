from uuid import UUID
from dataclasses import dataclass

from src.domain.entities.base import BaseEntity
from src.domain.descriptors import Text, Title


@dataclass
class Post(BaseEntity):
    title: Title
    text: Text
    user_id: str
    