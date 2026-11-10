import pytest
from Code. Find_Max_Min_List import find_max_min


def test_positive_numbers():
    assert find_max_min([10, 25, 5, 40, 15]) == (40, 5)


def test_single_element():
    assert find_max_min([10]) == (10, 10)


def test_negative_numbers():
    assert find_max_min([-5, -10, -2]) == (-2, -10)


def test_empty_list():
    with pytest.raises(ValueError):
        find_max_min([])