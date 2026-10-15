
from Code.Check_Palindrome_Number import check_palindrome


def test_palindrome_three_digit_number():
    assert check_palindrome(121) == True


def test_palindrome_four_digit_number():
    assert check_palindrome(1331) == True


def test_non_palindrome_number():
    assert check_palindrome(123) == False


def test_zero():
    assert check_palindrome(0) == True


def test_single_digit_number():
    assert check_palindrome(7) == True


def test_negative_number():
    assert check_palindrome(-121) == False

