import pytest

from src.infrastructure.repository.user.memory import UserMemoryRepository
from src.infrastructure.repository.post.memory import PostMemoryRepository
from src.infrastructure.repository.message.memory import MessageMemoryRepository


@pytest.fixture(scope='module')
def user_repo():
    return UserMemoryRepository()


@pytest.fixture(scope='module')
def post_repo():
    return PostMemoryRepository()


@pytest.fixture(scope='module')
def message_repo():
    return MessageMemoryRepository()
