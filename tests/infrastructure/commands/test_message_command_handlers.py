import pytest

from src.infrastructure.exceptions.command import InvalidCommandTypeException
from src.infrastructure.commands.message import CreateMessageCommand, CreateMessageCommandHandler, Message, MessageText, BaseMessageRepository
from src.domain.exceptions.descriptors import TooShortValueException


@pytest.fixture(scope='class')
def create_handler(message_repo):
    return CreateMessageCommandHandler(repository=message_repo)


class TestCreateMessageCommandHandler:
    @pytest.mark.asyncio
    async def test_create_user_command_success(self, message_repo: BaseMessageRepository, create_handler: CreateMessageCommandHandler):
        command: CreateMessageCommand = CreateMessageCommand(
            message='Simple text test',
            user_id='1'
        )
        message: Message = await create_handler.handle(command=command)
        assert message.user == command.user_id
        assert message.message == MessageText('Simple text test')

    @pytest.mark.asyncio
    async def test_create_user_command_success2(self, message_repo: BaseMessageRepository, create_handler: CreateMessageCommandHandler):
        command: CreateMessageCommand = CreateMessageCommand(
            message='Simple text test',
            user_id='123'
        )
        await create_handler.handle(command=command)
        assert len(await message_repo.get()) == 2

    @pytest.mark.asyncio
    async def test_create_user_command_invalid_username_failure(self, message_repo: BaseMessageRepository, create_handler: CreateMessageCommandHandler):
        command: CreateMessageCommand = CreateMessageCommand(
            message='',
            user_id='1234'
        )
        with pytest.raises(TooShortValueException):
            await create_handler.handle(command=command)

        assert len(await message_repo.get()) == 2
    
    @pytest.mark.asyncio
    async def test_create_user_command_invalid_command_failure2(self, message_repo: BaseMessageRepository, create_handler: CreateMessageCommandHandler):
        bad_command: str = 'Bad Bad Command'

        with pytest.raises(InvalidCommandTypeException): 
            await create_handler.handle(command=bad_command)
            