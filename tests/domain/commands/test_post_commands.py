import pytest

from src.domain.commands.post import CreatePostCommand, DeletePostCommand



class TestCreatePostCommand:
    def test_create_user_command_success(self):
        assert CreatePostCommand(title="hello", text="world", user_id=1)

    def test_create_user_command_invalid_username_failure(self):
        with pytest.raises(TypeError):
            CreatePostCommand()     

    def test_create_user_command_invalid_text_failure(self):
        with pytest.raises(TypeError):
            CreatePostCommand(title="hello", user_id=1)

    def test_create_user_command_invalid_title_failure(self):
        with pytest.raises(TypeError):
            CreatePostCommand(text="world", user_id=1)
            

class TestDeletePostCommand:
    def test_delete_user_command_success(self):
        assert DeletePostCommand(post_id='ehx')
    
    def test_delete_user_command_invalid_id_failure(self):
        with pytest.raises(TypeError):
            DeletePostCommand()
