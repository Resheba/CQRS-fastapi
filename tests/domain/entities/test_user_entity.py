import pytest

from src.domain.exceptions.descriptors import TooShortValueException
from src.domain.entities.user import User, Username


def test_user_success():
    assert User(username=Username("john"))


def test_invalid_username_failure():
    with pytest.raises(TooShortValueException):
        User(username=Username(""))
        