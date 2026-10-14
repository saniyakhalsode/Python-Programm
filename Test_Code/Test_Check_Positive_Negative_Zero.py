
from Code.Check_Positive_Negative_Zero import check_number


def test_positive_number():
    assert check_number(10) == "Positive"


def test_negative_number():
    assert check_number(-5) == "Negative"


def test_zero():
    assert check_number(0) == "Zero"


def test_large_positive_number():
    assert check_number(1000) == "Positive"


def test_large_negative_number():
    assert check_number(-1000) == "Negative"
