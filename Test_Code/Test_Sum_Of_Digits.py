
from Code.Sum_Of_Digits import sum_of_digits


def test_sum_of_four_digits():
    assert sum_of_digits(1234) == 10


def test_sum_of_three_digits():
    assert sum_of_digits(567) == 18


def test_single_digit():
    assert sum_of_digits(5) == 5


def test_zero():
    assert sum_of_digits(0) == 0


def test_number_with_zero_digits():
    assert sum_of_digits(1020) == 3


def test_negative_number():
    assert sum_of_digits(-123) == 6
