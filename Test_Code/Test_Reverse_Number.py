
from Code.Reverse_Number import reverse_number


def test_reverse_four_digit_number():
    assert reverse_number(1234) == 4321


def test_reverse_three_digit_number():
    assert reverse_number(567) == 765


def test_reverse_single_digit_number():
    assert reverse_number(5) == 5


def test_reverse_zero():
    assert reverse_number(0) == 0


def test_reverse_number_with_trailing_zeros():
    assert reverse_number(1200) == 21


def test_reverse_negative_number():
    assert reverse_number(-123) == -321

