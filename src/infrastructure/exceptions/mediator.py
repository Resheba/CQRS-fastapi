from dataclasses import dataclass

from src.infrastructure.exceptions.base import InfrastructureException


@dataclass(eq=False)
class MediatorException(InfrastructureException):
    _message: str = 'Mediator Exception'


class NoHandlerRegisteredException(MediatorException):
    _message: str = 'No handler registered'
