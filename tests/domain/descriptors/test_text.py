import pytest

from src.domain.exceptions.descriptors import TooShortValueException, TooLongValueException
from src.domain.descriptors.text import Text


def test_text_success():
    assert Text("hello")


def test_text_as_generic():
    assert Text("hello").as_generic() == "hello"


def test_invalid_text_failure1():
    with pytest.raises(TooShortValueException):
        Text("h")
    

def test_invalid_text_failure2():
    with pytest.raises(TooLongValueException):
        Text("hello world"*10)
