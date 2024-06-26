from dataclasses import dataclass

from src.domain.commands.base import BaseCommand


@dataclass(frozen=True)
class CreatePostCommand(BaseCommand):
    title: str
    text: str
    user_id: str
    

@dataclass(frozen=True)
class DeletePostCommand(BaseCommand):
    post_id: str
    