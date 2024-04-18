from pydantic.dataclasses import dataclass

from src.domain.descriptors.base import Descriptor
from src.domain.exceptions.descriptors import TooShortValueException


@dataclass(eq=False)
class Username(Descriptor[str]):
    def validate(self):
        if len(self.value) <= 3:
            raise TooShortValueException('Username is too short')
