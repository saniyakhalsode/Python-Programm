from Code.Check_Armstrong_Number import is_armstrong


def test_armstrong_number():
    assert is_armstrong(153) == True


def test_another_armstrong_number():
    assert is_armstrong(9474) == True


def test_non_armstrong_number():
    assert is_armstrong(123) == False


def test_negative_number():
    assert is_armstrong(-153) == False


def test_single_digit():
    assert is_armstrong(5) == True


def test_zero():
    assert is_armstrong(0) == True