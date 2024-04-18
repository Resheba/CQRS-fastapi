from dataclasses import dataclass

from domain.descriptors.username import Username
from domain.entities.base import BaseEntity


@dataclass
class User(BaseEntity):
    username: Username
    