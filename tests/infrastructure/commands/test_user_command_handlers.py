import pytest

from src.infrastructure.exceptions.command import InvalidCommandTypeException
from src.infrastructure.commands.user import DeleteUserCommandHandler
from src.infrastructure.repository.user.memory import UserMemoryRepository
from src.domain.exceptions.descriptors import TooLongValueException
from src.infrastructure.commands.user import CreateUserCommandHandler, CreateUserCommand, User, Username


@pytest.fixture(scope='class')
def create_handler(user_repo):
    return CreateUserCommandHandler(repository=user_repo)

@pytest.fixture(scope='class')
def delete_handler(user_repo):
    return DeleteUserCommandHandler(repository=user_repo)
    

class TestCreateUserCommandHandler:
    @pytest.mark.asyncio
    async def test_create_user_success(self, user_repo: UserMemoryRepository, create_handler: CreateUserCommandHandler):
        username = 'john'
        command = CreateUserCommand(username=username)

        created_user = await create_handler.handle(command=command)

        assert created_user.username == Username(username)
        assert created_user.id is not None
        assert len(await user_repo.get()) == 1

    @pytest.mark.asyncio
    async def test_create_user_invalid_username_failure(self, user_repo: UserMemoryRepository, create_handler: CreateUserCommandHandler):
        username = 'bad_boy'*100
        command = CreateUserCommand(username=username)

        with pytest.raises(TooLongValueException):
            await create_handler.handle(command=command)
        
        assert len(await user_repo.get()) == 1

    @pytest.mark.asyncio
    async def test_create_user_invalid_command_failure(self, user_repo: UserMemoryRepository, create_handler: CreateUserCommandHandler):
        bad_command: str = 'Bad Bad Command'

        with pytest.raises(InvalidCommandTypeException):
            await create_handler.handle(command=bad_command)


from src.infrastructure.commands.user import DeleteUserCommand


class TestDeleteUserCommandHandler:
    @pytest.mark.asyncio
    async def test_delete_user_success(self, user_repo: UserMemoryRepository, delete_handler: DeleteUserCommandHandler):
        user, *_ = await user_repo.get()
        user_id = user.id

        command = DeleteUserCommand(user_id=user_id)
        await delete_handler.handle(command=command)

        assert len(await user_repo.get()) == 0

    @pytest.mark.asyncio
    async def test_delete_user_invalid_user_id_failure(self):
        with pytest.raises(TypeError):
            DeleteUserCommand()
