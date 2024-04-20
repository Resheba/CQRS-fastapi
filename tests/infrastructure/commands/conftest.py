import pytest

from src.infrastructure.commands.user import CreateUserCommandHandler, DeleteUserCommandHandler
from src.infrastructure.repository.base.memory import BaseMemoryRepository


@pytest.fixture(scope='module')
def repo():
    return BaseMemoryRepository()


@pytest.fixture(scope='class')
def create_handler(repo):
    return CreateUserCommandHandler(repository=repo)


@pytest.fixture(scope='class')
def delete_handler(repo):
    return DeleteUserCommandHandler(repository=repo)
