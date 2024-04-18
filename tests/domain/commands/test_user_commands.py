import pytest

from src.domain.commands.user import CreateUserCommand, DeleteUserCommand


class TestCreateUserCommand:
    def test_create_user_command_success(self):
        assert CreateUserCommand("john")

    def test_create_user_command_invalid_username_failure(self):
        with pytest.raises(TypeError):
            CreateUserCommand()
            

class TestDeleteUserCommand:
    def test_delete_user_command_success(self):
        assert DeleteUserCommand("ehx")
    
    def test_delete_user_command_invalid_id_failure(self):
        with pytest.raises(TypeError):
            DeleteUserCommand()
