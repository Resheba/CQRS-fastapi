from dataclasses import dataclass

from src.domain.commands.base import BaseCommand


@dataclass(frozen=True)
class CreateMessageCommand(BaseCommand):
    message: str
    user_id: str
    