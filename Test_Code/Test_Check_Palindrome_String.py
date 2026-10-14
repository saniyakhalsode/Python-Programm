from Code.Check_Palindrome_String import is_palindrome

def test_palindrome_word():
    assert is_palindrome("madam") is True

def test_palindrome_level():
    assert is_palindrome("level") is True

def test_non_palindrome_word():
    assert is_palindrome("hello") is False

def test_single_character():
    assert is_palindrome("a") is True

def test_empty_string():
    assert is_palindrome("") is True

def test_uppercase_string():
    assert is_palindrome("MADAM") is True
 