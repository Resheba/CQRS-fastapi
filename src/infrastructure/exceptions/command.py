from dataclasses import dataclass

from src.infrastructure.exceptions.base import InfrastructureException


@dataclass(eq=False)
class CommandException(InfrastructureException):
    _message: str = 'Command exception'


@dataclass(eq=False)
class InvalidCommandTypeException(CommandException):
    _message: str = 'Invalid command type'
