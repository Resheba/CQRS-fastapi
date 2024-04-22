from punq import Container, Scope

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
from src.infrastructure.mediator import Mediator


def setup_mediator() -> Mediator:
    mediator: Mediator = Mediator()
    container: Container = setup_container()

    mediator.register_command(CreateMessageCommand, [container.resolve(CreateMessageCommandHandler)])
    mediator.register_command(CreatePostCommand, [container.resolve(CreatePostCommandHandler)])
    mediator.register_command(CreateUserCommand, [container.resolve(CreateUserCommandHandler)])
    mediator.register_command(DeletePostCommand, [container.resolve(DeletePostCommandHandler)])
    mediator.register_command(DeleteUserCommand, [container.resolve(DeleteUserCommandHandler)])
    mediator.register_query(GetUserQuery, [container.resolve(GetUserQueryHandler)])
    mediator.register_query(GetPostQuery, [container.resolve(GetPostQueryHandler)])
    mediator.register_query(GetMessageQuery, [container.resolve(GetMessageQueryHandler)])

    return mediator


def setup_container() -> Container:
    container: Container = Container()
    container.register(BaseMessageRepository, MessageMemoryRepository, scope=Scope.singleton)
    container.register(BasePostRepository, PostMemoryRepository, scope=Scope.singleton)
    container.register(BaseUserRepository, UserMemoryRepository, scope=Scope.singleton)
    
    container.register(CreateMessageCommandHandler)
    container.register(CreatePostCommandHandler)
    container.register(CreateUserCommandHandler)
    container.register(DeletePostCommandHandler)
    container.register(DeleteUserCommandHandler)
    container.register(GetUserQueryHandler)
    container.register(GetPostQueryHandler)
    container.register(GetMessageQueryHandler)
    
    return container
