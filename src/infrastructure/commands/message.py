from dataclasses import dataclass

from src.domain.commands.message import CreateMessageCommand
from src.domain.entities.message import Message, MessageText
from src.infrastructure.commands.base import BaseCommandHandler
from src.infrastructure.repository.base.base import BaseRepository


@dataclass(frozen=True)
class CreateMessageCommandHandler(BaseCommandHandler[CreateMessageCommand, Message]):
    repository: BaseRepository

    async def handle(self, command: CreateMessageCommand) -> Message:
        message_text: MessageText = MessageText(command.message)
        message: Message = Message(message=message_text, user=command.user_id)
        await self.repository.add(message.dict())
        return message
