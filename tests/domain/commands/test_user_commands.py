import pytest

from src.domain.commands.user import CreateUserCommand


def test_create_user_command_success():
    assert CreateUserCommand("john")


def test_create_user_command_invalid_username_failure():
    with pytest.raises(TypeError):
        CreateUserCommand()
        