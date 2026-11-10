from Code.Find_Sum_List import find_sum


def test_positive_numbers():
    assert find_sum([10, 20, 30]) == 60


def test_negative_numbers():
    assert find_sum([-5, -10, -15]) == -30


def test_empty_list():
    assert find_sum([]) == 0


def test_single_element():
    assert find_sum([25]) == 25