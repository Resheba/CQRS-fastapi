from pydantic.dataclasses import dataclass

from src.domain.descriptors.base import Descriptor
from src.domain.exceptions.descriptors import TooShortValueException, TooLongValueException


@dataclass(eq=False)
class Title(Descriptor[str]):
    def validate(self) -> None:
        if len(self.value) <= 3:
            raise TooShortValueException('title is too short')
        elif len(self.value) > 30:
            raise TooLongValueException('title is too long')
