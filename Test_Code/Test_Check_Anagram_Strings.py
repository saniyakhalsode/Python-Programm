from Code.Check_Anagram_Strings import check_anagram


def test_anagram():
    assert check_anagram("listen", "silent") == True


def test_not_anagram():
    assert check_anagram("hello", "world") == False


def test_uppercase():
    assert check_anagram("LISTEN", "silent") == True


def test_ignore_spaces():
    assert check_anagram("Dormitory", "Dirty room") == True


def test_empty_strings():
    assert check_anagram("", "") == True


def test_different_length():
    assert check_anagram("abc", "abcd") == False