from dataclasses import dataclass

from src.domain.commands.message import CreateMessageCommand
from src.domain.entities.message import Message, MessageText
from src.infrastructure.commands.base import BaseCommandHandler
from src.infrastructure.repository.message.base import BaseMessageRepository


@dataclass(frozen=True)
class CreateMessageCommandHandler(BaseCommandHandler[CreateMessageCommand, Message]):
    repository: BaseMessageRepository

    async def handle(self, command: CreateMessageCommand) -> Message:
        await super().handle(command)
        message_text: MessageText = MessageText(command.message)
        message: Message = Message(message=message_text, user=command.user_id)
        await self.repository.add(message)
        return message
