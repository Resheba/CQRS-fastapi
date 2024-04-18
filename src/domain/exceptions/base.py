from dataclasses import dataclass, field


@dataclass(eq=False)
class DomainException(Exception):
    _message: str = field(default='Domain exception')
    @property
    def message(self):
        return self._message
