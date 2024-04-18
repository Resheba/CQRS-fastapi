import pytest

from src.domain.entities.user import User
from src.domain.descriptors.username import Username
from src.domain.events.user import UserCreated


def test_user_created_success():
    username = Username("john")
    user = User(username=username)

    event = UserCreated(user=user)

    assert event.user.id == user.id


def test_user_created_invalid_username_failure():
    with pytest.raises(TypeError):
        UserCreated()
