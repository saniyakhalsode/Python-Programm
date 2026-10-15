
from Code.Print_Prime_Numbers_In_Range import print_prime_numbers


def test_prime_numbers_from_one_to_ten():
    assert print_prime_numbers(1, 10) == [2, 3, 5, 7]


def test_prime_numbers_from_one_to_twenty():
    assert print_prime_numbers(1, 20) == [2, 3, 5, 7, 11, 13, 17, 19]


def test_range_with_no_prime_numbers():
    assert print_prime_numbers(8, 10) == []


def test_range_containing_two():
    assert print_prime_numbers(2, 5) == [2, 3, 5]


def test_negative_starting_number():
    assert print_prime_numbers(-5, 5) == [2, 3, 5]


def test_single_prime_number():
    assert print_prime_numbers(7, 7) == [7]

