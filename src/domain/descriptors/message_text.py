from pydantic.dataclasses import dataclass

from src.domain.descriptors.base import Descriptor
from src.domain.exceptions.descriptors import TooShortValueException, TooLongValueException


@dataclass(eq=False)
class MessageText(Descriptor[str]):
    def validate(self) -> None:
        if len(self.value) == 0:
            raise TooShortValueException('message is empty')
        elif len(self.value) > 100:
            raise TooLongValueException('message is too long')
