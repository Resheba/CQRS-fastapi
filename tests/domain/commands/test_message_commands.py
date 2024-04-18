import pytest

from src.domain.commands.message import CreateMessageCommand


class TestCreateMessageCommand:
    def test_create_user_command_success(self):
        assert CreateMessageCommand(message="hello", user_id=1)
    
    def test_create_user_command_invalid_username_failure(self):
        with pytest.raises(TypeError):
            CreateMessageCommand()
