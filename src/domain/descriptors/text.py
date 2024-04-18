from pydantic.dataclasses import dataclass

from src.domain.descriptors.base import Descriptor
from src.domain.exceptions.descriptors import TooShortValueException, TooLongValueException


@dataclass(eq=False)
class Text(Descriptor[str]):
    def validate(self) -> None:
        if len(self.value) <= 3:
            raise TooShortValueException('text is too short')
        elif len(self.value) > 100:
            raise TooLongValueException('text is too long')
