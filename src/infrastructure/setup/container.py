from punq import Container

from src.infrastructure.repository import (
    BaseMessageRepository, 
    MessageMemoryRepository,
    BasePostRepository,
    PostMemoryRepository,
    BaseUserRepository,
    UserMemoryRepository,
)
from src.infrastructure.commands import (
    CreateMessageCommand,
    CreateMessageCommandHandler,
    CreatePostCommand,
    CreatePostCommandHandler,
    CreateUserCommand,
    CreateUserCommandHandler,
    DeletePostCommand,
    DeletePostCommandHandler,
    DeleteUserCommand,
    DeleteUserCommandHandler ,
)
from src.infrastructure.queries import (
    GetUserQuery,
    GetUserQueryHandler,
    GetPostQuery,
    GetPostQueryHandler,
    GetMessageQuery,
    GetMessageQueryHandler,
)


def setup_container() -> Container:
    ...