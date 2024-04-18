from dataclasses import dataclass

from src.domain.descriptors.username import Username
from src.domain.entities.base import BaseEntity


@dataclass
class User(BaseEntity):
    username: Username
    