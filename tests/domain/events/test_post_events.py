import pytest
from uuid import UUID

from src.domain.entities.post import Post
from src.domain.descriptors import Text, Title
from src.domain.events.post import PostCreated, PostDeleted
from src.domain.exceptions.descriptors import TooLongValueException, TooShortValueException


class TestPostCreatedEvent:
    def test_post_created_success(self):
        title = Title("hello")
        text = Text("world")
        post = Post(title=title, text=text, user_id=UUID(int=1))
        assert PostCreated(post=post)

    def test_post_created_invalid_title_failure(self):
        with pytest.raises(TooShortValueException):
            PostCreated(post=Post(title=Title("h"), text=Text("world"), user_id=UUID(int=1)))

    def test_post_created_invalid_text_failure(self):
        with pytest.raises(TooLongValueException):
            PostCreated(post=Post(title=Title("hello"), text=Text("world"*100), user_id=UUID(int=1)))

    def test_post_created_invalid_field_failure(self):
        with pytest.raises(TypeError):
            PostCreated()


class TestPostDeletedEvent:
    def test_post_deleted_success(self):
        assert PostDeleted(title='hello')

    def test_post_deleted_invalid_title_failure(self):
        with pytest.raises(TypeError):
            PostDeleted()
    