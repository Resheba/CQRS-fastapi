from dataclasses import dataclass

from src.domain.entities.user import User, Username
from src.domain.commands.user import CreateUserCommand, DeleteUserCommand
from src.infrastructure.repository.user.base import BaseUserRepository
from src.infrastructure.commands.base import BaseCommandHandler


@dataclass(frozen=True)
class CreateUserCommandHandler(BaseCommandHandler[CreateUserCommand, User]):
    repository: BaseUserRepository

    async def handle(self, command: CreateUserCommand) -> User:
        username: Username = Username(command.username)
        user: User = User(username=username)
        await self.repository.add(user)
        return user
    

@dataclass(frozen=True)
class DeleteUserCommandHandler(BaseCommandHandler[DeleteUserCommand, None]):
    repository: BaseUserRepository

    async def handle(self, command: DeleteUserCommand) -> None:
        await self.repository.delete(command.user_id)
