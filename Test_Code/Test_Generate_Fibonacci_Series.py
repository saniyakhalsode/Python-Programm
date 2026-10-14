
from Code.Generate_Fibonacci_Series import generate_fibonacci


def test_fibonacci_five_terms():
    assert generate_fibonacci(5) == [0, 1, 1, 2, 3]


def test_fibonacci_one_term():
    assert generate_fibonacci(1) == [0]


def test_fibonacci_two_terms():
    assert generate_fibonacci(2) == [0, 1]


def test_fibonacci_zero_terms():
    assert generate_fibonacci(0) == []


def test_fibonacci_negative_terms():
    assert generate_fibonacci(-3) == []
