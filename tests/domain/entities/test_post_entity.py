import pytest

from src.domain.exceptions.descriptors import TooShortValueException, TooLongValueException
from src.domain.entities.post import Post, Text, Title, UUID


def test_post_success():
    assert Post(title=Title("hello"), text=Text("world"), user_id=UUID(int=1))


def test_no_title_failure():
    with pytest.raises(TypeError):
        Post(text=Text("world"), user_id=UUID(int=1))


def test_no_text_failure():
    with pytest.raises(TypeError):
        Post(title=Title("hello"), user_id=UUID(int=1))


def test_invalid_title_failure1():
    with pytest.raises(TooShortValueException):
        Post(title=Title("h"), text=Text("world"), user_id=UUID(int=1))


def test_invalid_title_failure2():
    with pytest.raises(TooLongValueException):
        Post(title=Title("hello world"*10), text=Text("world"), user_id=UUID(int=1))


def test_invalid_text_failure1():
    with pytest.raises(TooShortValueException): 
        Post(title=Title("hello"), text=Text("h"), user_id=UUID(int=1))
        