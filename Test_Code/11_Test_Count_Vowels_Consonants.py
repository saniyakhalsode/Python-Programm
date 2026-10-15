
from Code.Count_Vowels_Consonants import count_vowels_consonants


def test_hello_world():
    assert count_vowels_consonants("Hello World") == (3, 7)


def test_all_vowels():
    assert count_vowels_consonants("aeiou") == (5, 0)


def test_all_consonants():
    assert count_vowels_consonants("bcdfg") == (0, 5)


def test_empty_string():
    assert count_vowels_consonants("") == (0, 0)


def test_numbers_and_symbols():
    assert count_vowels_consonants("abc123!") == (1, 2)


def test_uppercase_letters():
    assert count_vowels_consonants("AEIOU") == (5, 0)

