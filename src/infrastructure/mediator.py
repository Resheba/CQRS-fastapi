from collections import defaultdict
from dataclasses import dataclass, field
from typing import Iterable

from src.infrastructure.exceptions.mediator import NoHandlerRegisteredException
from src.infrastructure.commands.base import CT, RT as CR,  BaseCommandHandler
from src.infrastructure.queries.base import QT, RT as QR, BaseQueryHandler


@dataclass(eq=False)
class Mediator:
    _commands_map: defaultdict[CT, list[BaseCommandHandler]] = field(
        default_factory=lambda: defaultdict(list),
        kw_only=True,
    )
    _query_map: defaultdict[QT, list[BaseQueryHandler]] = field(
        default_factory=lambda: defaultdict(list),
        kw_only=True,
    )

    def register_command(self, command: CT, handler: Iterable[BaseCommandHandler]) -> None:
        self._commands_map[command].extend(handler)
    
    def register_query(self, query: QT, handler: Iterable[BaseQueryHandler]) -> None:
        self._query_map[query].extend(handler)
    
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
    