import pytest

from src.domain.entities.user import User
from src.domain.descriptors.username import Username
from src.domain.events.user import UserCreated, UserDeleted


class TestUserCreatedEvent:
    def test_user_created_success(self):
        username = Username("john")
        user = User(username=username)

        event = UserCreated(user=user)

        assert event.user.id == user.id

    def test_user_created_invalid_username_failure(self):
        with pytest.raises(TypeError):
            UserCreated()


class TestUserDeletedEvent:
    def test_user_deleted_success(self):
        username = "john"
        event = UserDeleted(username=username)

        assert event.username == username
    
    def test_user_deleted_invalid_username_failure(self):
        with pytest.raises(TypeError):
            UserDeleted()
            