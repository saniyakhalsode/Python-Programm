from Code.Find_Second_Largest_Number import find_second_largest

def test_normal_list():
    assert find_second_largest([10, 25, 8, 40, 15]) == 25

def test_second_largest_at_beginning():
    assert find_second_largest([20, 10, 5, 2]) == 10

def test_negative_numbers():
    assert find_second_largest([-10, -5, -20, -2]) == -5

def test_duplicate_numbers():
    assert find_second_largest([10, 10, 8, 8, 5]) == 8

def test_only_one_unique_number():
    assert find_second_largest([5, 5, 5]) is None

def test_two_numbers():
    assert find_second_largest([4, 9]) == 4

def test_empty_list():
    assert find_second_largest([]) is None
