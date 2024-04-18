from pydantic.dataclasses import dataclass

from src.domain.descriptors.base import Descriptor
from src.domain.exceptions.descriptors import TooLongValueException, TooShortValueException


@dataclass(eq=False)
class Username(Descriptor[str]):
    def validate(self) -> None:
        if len(self.value) <= 3:
            raise TooShortValueException('username is too short')
        elif len(self.value) > 20:
            raise TooLongValueException('username is too long')
