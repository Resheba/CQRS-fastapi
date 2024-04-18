from dataclasses import dataclass

from src.domain.entities.post import Post
from src.domain.events.base import BaseEvent


@dataclass(frozen=True)
class PostCreated(BaseEvent):
    post: Post
    