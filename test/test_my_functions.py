import pytest
import source.my_functions as my_functions


def test_add():
    result: float = my_functions.add(2, 3)
    assert result == 5


def test_divide():
    result: float = my_functions.divide(10, 2)
    assert result == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        result: float = my_functions.divide(10, 0)
