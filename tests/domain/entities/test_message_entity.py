import pytest

from src.domain.exceptions.descriptors import TooShortValueException, TooLongValueException
from src.domain.entities.message import Message, MessageText, UUID


def test_message_success():
    assert Message(message=MessageText("hello"), user=UUID(int=1))


def test_no_message_failure():
    with pytest.raises(TypeError):
        Message(user=UUID(int=1))


def test_invalid_message_failure1():
    with pytest.raises(TooShortValueException):
        Message(message=MessageText(""), user=UUID(int=1))


def test_invalid_message_failure2():
    with pytest.raises(TooLongValueException):
        Message(message=MessageText("hello worldrg"*10), user=UUID(int=1))
