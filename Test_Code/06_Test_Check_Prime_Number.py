
from Code.Check_Prime_Number import check_prime


def test_prime_number():
    assert check_prime(7) == True


def test_non_prime_number():
    assert check_prime(8) == False


def test_number_two():
    assert check_prime(2) == True


def test_number_one():
    assert check_prime(1) == False


def test_zero():
    assert check_prime(0) == False


def test_negative_number():
    assert check_prime(-5) == False


def test_large_prime_number():
    assert check_prime(97) == True

