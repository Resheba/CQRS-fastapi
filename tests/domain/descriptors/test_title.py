import pytest

from src.domain.exceptions.descriptors import TooShortValueException, TooLongValueException
from src.domain.descriptors.title import Title


def test_title_success():
    assert Title("hello")


def test_invalid_title_failure1():
    with pytest.raises(TooShortValueException):
        Title("h")


def test_invalid_title_failure2():
    with pytest.raises(TooLongValueException):
        Title("hello world"*10)


def test_title_as_generic():
    assert Title("hello").as_generic() == "hello"