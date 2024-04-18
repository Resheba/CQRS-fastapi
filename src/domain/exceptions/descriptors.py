from dataclasses import dataclass

from src.domain.exceptions.base import DomainException


@dataclass(eq=False)
class TooShortValueException(DomainException):
    _message: str = 'Value is too short'
