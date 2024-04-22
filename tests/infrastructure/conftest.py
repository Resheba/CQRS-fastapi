import pytest

from src.infrastructure.repository.base.memory import BaseMemoryRepository


@pytest.fixture(scope='module')
def repo():
    BaseMemoryRepository.storage = list()
    return BaseMemoryRepository()
