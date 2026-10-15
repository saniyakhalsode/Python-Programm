from Code.Word_Frequency_In_A_Sentence import word_frequency

def test_repeated_words():
 assert word_frequency("python is easy and python is powerful") == {
"python": 2,
"is": 2,
"easy": 1,
"and": 1,
"powerful": 1
}

def test_single_word():
 assert word_frequency("hello") == {"hello": 1}

def test_empty_sentence():
 assert word_frequency("") == {}

def test_case_insensitive():
 assert word_frequency("Python python PYTHON") == {"python": 3}

def test_all_words_repeated():
 assert word_frequency("hi hi hi") == {"hi": 3}

def test_extra_spaces():
 assert word_frequency("hello   world hello") == {
"hello": 2,
"world": 1
}
