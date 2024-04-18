import pytest

from src.domain.exceptions.descriptors import TooShortValueException, TooLongValueException
from src.domain.descriptors.message_text import MessageText


def test_message_success():
    assert MessageText("hello")


def test_message_as_generic():
    assert MessageText("hello").as_generic() == "hello"


def test_invalid_message_failure1():
    with pytest.raises(TooShortValueException):
        MessageText("")
    

def test_invalid_message_failure2():
    with pytest.raises(TooLongValueException):
        MessageText("hello worldrg"*10)
