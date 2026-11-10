import pytest
from Code.Decimal_To_Binary import decimal_to_binary


def test_positive_number():
    assert decimal_to_binary(10) == "1010"


def test_another_number():
    assert decimal_to_binary(25) == "11001"


def test_zero():
    assert decimal_to_binary(0) == "0"


def test_one():
    assert decimal_to_binary(1) == "1"


def test_negative_number():
    with pytest.raises(ValueError):
        decimal_to_binary(-5)


def test_large_number():
    assert decimal_to_binary(100) == "1100100"