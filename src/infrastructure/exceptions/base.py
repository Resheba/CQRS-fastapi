from dataclasses import dataclass, field


@dataclass(eq=False)
class InfrastructureException(Exception):
    _message: str = field(default='Infrastructure exception')
    @property
    def message(self):
        return self._message
