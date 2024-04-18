import pytest

from src.domain.descriptors.username import Username
from src.domain.exceptions.descriptors import TooShortValueException, TooLongValueException


def test_username_success():
    assert Username("john")


def test_username_as_generic():
    assert Username("jane").as_generic() == "jane"
    assert Username("john").as_generic() == "john"


def test_invalid_username_failure():
    with pytest.raises(TooShortValueException):
        Username("jo")
    

def test_invalid_username_failure_2():
    with pytest.raises(TooLongValueException):
        Username("a"*30)

