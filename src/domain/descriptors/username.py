from pydantic.dataclasses import dataclass

from .base import Descriptor
from ..exceptions.descriptors import TooShortValueException


@dataclass(eq=False)
class Username(Descriptor[str]):
    def validate(self):
        if len(self.value) <= 3:
            raise TooShortValueException('Username is too short')
