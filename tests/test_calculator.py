import pytest

from calculator import Calculator


def test_add() -> None:
    assert Calculator().add(10, 2) == 12


def test_subtract() -> None:
    assert Calculator().subtract(10, 2) == 8


def test_multiply() -> None:
    assert Calculator().multiply(10, 2) == 20


def test_divide() -> None:
    assert Calculator().divide(10, 2) == 5


def test_divide_by_zero() -> None:
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        Calculator().divide(10, 0)
