from dataclasses import dataclass

from src.domain.entities.user import User, Username
from src.domain.commands.user import CreateUserCommand, DeleteUserCommand
from src.infrastructure.repository.base.base import BaseRepository
from src.infrastructure.commands.base import BaseCommandHandler


@dataclass
class CreateUserCommandHandler(BaseCommandHandler[CreateUserCommand, User]):
    repository: BaseRepository

    async def handle(self, command: CreateUserCommand) -> User:
        username: Username = Username(command.username)
        user: User = User(username=username)
        await self.repository.add(user.dict())
        return User
    

@dataclass
class DeleteUserCommandHandler(BaseCommandHandler[DeleteUserCommand, None]):
    repository: BaseRepository

    async def handle(self, command: DeleteUserCommand) -> None:
        await self.repository.delete(command.user_id)
        