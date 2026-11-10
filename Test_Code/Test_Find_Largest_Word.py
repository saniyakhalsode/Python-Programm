from Code.Find_Largest_Word import find_largest_word


def test_largest_word():
    assert find_largest_word("Python programming is interesting") == "programming"


def test_ignore_punctuation():
    assert find_largest_word("I love beautiful flowers!") == "beautiful"


def test_same_length():
    assert find_largest_word("apple mango banana") == "banana"


def test_empty_sentence():
    assert find_largest_word("") == ""


def test_single_word():
    assert find_largest_word("Python") == "Python"


def test_only_punctuation():
    assert find_largest_word("!!! ??? ...") == ""


def test_first_word_on_tie():
    assert find_largest_word("cat dog bird") == "bird"