
from Code.Largest_Of_Three_Num import find_largest


def test_first_number_largest():
    assert find_largest(30, 20, 10) == 30


def test_second_number_largest():
    assert find_largest(10, 40, 20) == 40


def test_third_number_largest():
    assert find_largest(10, 20, 50) == 50


def test_all_numbers_equal():
    assert find_largest(5, 5, 5) == 5


def test_negative_numbers():
    assert find_largest(-10, -5, -20) == -5
