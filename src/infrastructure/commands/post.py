from dataclasses import dataclass

from src.domain.entities.post import Post, Text, Title
from src.domain.commands.post import CreatePostCommand, DeletePostCommand
from src.infrastructure.repository.post.base import BasePostRepository
from src.infrastructure.commands.base import BaseCommandHandler


@dataclass(frozen=True)
class CreatePostCommandHandler(BaseCommandHandler[CreatePostCommand, Post]):
    repository: BasePostRepository

    async def handle(self, command: CreatePostCommand) -> Post:
        await super().handle(command)
        title: Title = Title(command.title)
        text: Text = Text(command.text)
        post: Post = Post(title=title, text=text, user_id=command.user_id)
        await self.repository.add(post)
        return post
    

@dataclass(frozen=True)
class DeletePostCommandHandler(BaseCommandHandler[DeletePostCommand, None]):
    repository: BasePostRepository

    async def handle(self, command: DeletePostCommand) -> None:
        await super().handle(command)
        await self.repository.delete(command.post_id)
