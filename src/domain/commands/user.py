from dataclasses import dataclass

from src.domain.commands.base import BaseCommand


@dataclass(frozen=True)
class CreateUserCommand(BaseCommand):
    username: str
    