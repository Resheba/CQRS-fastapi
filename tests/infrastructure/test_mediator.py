import pytest
from unittest.mock import AsyncMock

from src.infrastructure.mediator import Mediator
from src.infrastructure.commands.user import CreateUserCommand, CreateUserCommandHandler, User
from src.infrastructure.queries.user import GetUserQueryHandler, GetUserQuery
from src.infrastructure.exceptions.mediator import NoHandlerRegisteredException


@pytest.fixture
def mediator():
    return Mediator()


@pytest.fixture
def create_handler():
    return CreateUserCommandHandler(AsyncMock())


@pytest.fixture
def query_handler():
    return GetUserQueryHandler(AsyncMock())


class TestMediator:
    @pytest.mark.asyncio
    async def test_mediator_register_command(self, mediator: Mediator, create_handler: CreateUserCommandHandler):
        mediator.register_command(CreateUserCommand, [create_handler])
        assert mediator._commands_map[CreateUserCommand] == [create_handler]

    @pytest.mark.asyncio
    async def test_mediator_register_query(self, mediator: Mediator, query_handler: GetUserQueryHandler):
        mediator.register_query(GetUserQuery, [query_handler])
        assert mediator._query_map[GetUserQuery] == [query_handler]

    @pytest.mark.asyncio
    async def test_mediator_handle_command(self, mediator: Mediator, create_handler: CreateUserCommandHandler):
        mediator.register_command(CreateUserCommand, [create_handler])
        users: list[User] = await mediator.handle_command(CreateUserCommand(username='john'))
        assert len(users) == 1
        assert users[0].username.as_generic() == 'john'
    
    @pytest.mark.asyncio
    async def test_mediator_handle_query(self, mediator: Mediator, query_handler: GetUserQueryHandler):
        mediator.register_query(GetUserQuery, [query_handler])
        users: list[tuple[User]] = await mediator.handle_query(GetUserQuery())
        assert len(users) == 1
        assert len(users[0]) == 0

    @pytest.mark.asyncio
    async def test_mediator_handle_invalid_command(self, mediator: Mediator):
        with pytest.raises(NoHandlerRegisteredException):
            await mediator.handle_command(CreateUserCommand('john'))
    
    @pytest.mark.asyncio
    async def test_mediator_handle_invalid_query(self, mediator: Mediator):
        with pytest.raises(NoHandlerRegisteredException):
            await mediator.handle_query(GetUserQuery())

    def test_singleton(self):
        assert id(Mediator()) == id(Mediator())
