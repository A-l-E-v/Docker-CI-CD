import pytest
from simple_library_01.functions import is_leap


def test_zero_year_raises_error():
    with pytest.raises(AttributeError):
        is_leap(0)


def test_negative_year_raises_error():
    with pytest.raises(AttributeError):
        is_leap(-100)
