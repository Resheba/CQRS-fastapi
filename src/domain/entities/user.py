from dataclasses import dataclass

from src.domain.descriptors import Username
from src.domain.entities.base import BaseEntity


@dataclass
class User(BaseEntity):
    username: Username

    def dict(self) -> dict:
        return {'id': self.id, 'username': self.username.value}
    