import pytest
from uuid import UUID

from src.domain.entities.post import Post
from src.domain.descriptors import Text, Title
from src.domain.events.post import PostCreated
from src.domain.exceptions.descriptors import TooLongValueException, TooShortValueException


def test_post_created_success():
    title = Title("hello")
    text = Text("world")
    post = Post(title=title, text=text, user_id=UUID(int=1))
    assert PostCreated(post=post)


def test_post_created_invalid_title_failure():
    with pytest.raises(TooShortValueException):
        PostCreated(post=Post(title=Title("h"), text=Text("world"), user_id=UUID(int=1)))


def test_post_created_invalid_text_failure():
    with pytest.raises(TooLongValueException):
        PostCreated(post=Post(title=Title("hello"), text=Text("world"*100), user_id=UUID(int=1)))


def test_post_created_invalid_field_failure():
    with pytest.raises(TypeError):
        PostCreated()
