from dataclasses import dataclass

from src.domain.entities.post import Post, Text, Title
from src.domain.commands.post import CreatePostCommand, DeletePostCommand
from src.infrastructure.repository.base.base import BaseRepository
from src.infrastructure.commands.base import BaseCommandHandler


@dataclass(frozen=True)
class CreatePostCommandHandler(BaseCommandHandler[CreatePostCommand, Post]):
    repository: BaseRepository

    async def handle(self, command: CreatePostCommand) -> Post:
        title: Title = Title(command.title)
        text: Text = Text(command.text)
        post: Post = Post(title=title, text=text, user_id=command.user_id)
        await self.repository.add(post)
        return post
    

@dataclass(frozen=True)
class DeletePostCommandHandler(BaseCommandHandler[DeletePostCommand, None]):
    repository: BaseRepository

    async def handle(self, command: DeletePostCommand) -> None:
        await self.repository.delete(command.post_id)
