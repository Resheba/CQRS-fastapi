import pytest

from src.domain.commands.post import CreatePostCommand


def test_create_user_command_success():
    assert CreatePostCommand(title="hello", text="world", user_id=1)


def test_create_user_command_invalid_username_failure():
    with pytest.raises(TypeError):
        CreatePostCommand()
        

def test_create_user_command_invalid_text_failure():
    with pytest.raises(TypeError):
        CreatePostCommand(title="hello", user_id=1)


def test_create_user_command_invalid_title_failure():
    with pytest.raises(TypeError):
        CreatePostCommand(text="world", user_id=1)
        