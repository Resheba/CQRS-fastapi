from typing import Generic, TypeVar
from abc import ABC, abstractmethod
from pydantic.dataclasses import dataclass


DT = TypeVar('DT')

@dataclass
class Descriptor(ABC, Generic[DT]):
    value: DT

    def __post_init__(self):
        self.validate()

    @abstractmethod
    def validate(self):
        ...

    def as_generic(self) -> DT:
        return self.value
