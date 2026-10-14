
from Code.Reverse_String import reverse_string


def test_reverse_word():
    assert reverse_string("Hello") == "olleH"


def test_reverse_python():
    assert reverse_string("Python") == "nohtyP"


def test_single_character():
    assert reverse_string("A") == "A"


def test_empty_string():
    assert reverse_string("") == ""


def test_reverse_sentence():
    assert reverse_string("Hello World") == "dlroW olleH"


def test_reverse_numbers_as_string():
    assert reverse_string("12345") == "54321"
