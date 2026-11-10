from Code.Sort_List_Without_Sort import sort_list


def test_normal_list():
    assert sort_list([5, 2, 8, 1, 3]) == [1, 2, 3, 5, 8]


def test_already_sorted():
    assert sort_list([1, 2, 3, 4]) == [1, 2, 3, 4]


def test_reverse_list():
    assert sort_list([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_duplicate_numbers():
    assert sort_list([4, 2, 4, 1, 2]) == [1, 2, 2, 4, 4]


def test_empty_list():
    assert sort_list([]) == []


def test_single_element():
    assert sort_list([7]) == [7]


def test_original_list_unchanged():
    numbers = [5, 3, 1, 4, 2]
    sort_list(numbers)
    assert numbers == [5, 3, 1, 4, 2]