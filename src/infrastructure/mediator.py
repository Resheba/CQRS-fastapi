from collections import defaultdict
from dataclasses import dataclass, field
from typing import Iterable

from src.infrastructure.exceptions.mediator import NoHandlerRegisteredException
from src.infrastructure.commands.base import CT, RT as CR,  BaseCommandHandler
from src.infrastructure.queries.base import QT, RT as QR, BaseQueryHandler


@dataclass(eq=False, init=False)
class Mediator:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Mediator, cls).__new__(cls, *args, **kwargs)
            cls._inicialized = False
        return cls._instance
    
    def __init__(self) -> None:
        if not self._inicialized:
            self._commands_map: defaultdict[CT, set[BaseCommandHandler]] = defaultdict(set)
            self._query_map: defaultdict[QT, set[BaseQueryHandler]] = defaultdict(set)
            self._inicialized = True
    
    def _reset(self) -> None:
        self._commands_map: defaultdict[CT, set[BaseCommandHandler]] = defaultdict(set)
        self._query_map: defaultdict[QT, set[BaseQueryHandler]] = defaultdict(set)

    def register_command(self, command: CT, handlers: Iterable[BaseCommandHandler]) -> None:
        self._commands_map[command].update(handlers)
    
    def register_query(self, query: QT, handlers: Iterable[BaseQueryHandler]) -> None:
        self._query_map[query].update(handlers)
    
    async def handle_command(self, command: CT) -> Iterable[CR]:
        handlers: list[BaseCommandHandler] = self._commands_map[command.__class__]

        if not handlers:
            raise NoHandlerRegisteredException(f'No handler registered for {command.__class__}')
        return [await handler.handle(command) for handler in handlers]

    async def handle_query(self, query: QT) -> Iterable[QR]:
        handlers: list[BaseQueryHandler] = self._query_map[query.__class__]

        if not handlers:
            raise NoHandlerRegisteredException(f'No handler registered for {query.__class__}')
        return [await handler.handle(query) for handler in handlers]
    