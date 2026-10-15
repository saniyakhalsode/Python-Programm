from Code.Find_Duplicate_Elements import find_duplicates

def test_normal_list():
 assert find_duplicates([1, 2, 3, 2, 4, 1, 5]) == [1, 2]

def test_no_duplicates():
 assert find_duplicates([1, 2, 3, 4]) == []

def test_all_duplicates():
 assert find_duplicates([5, 5, 5]) == [5]

def test_empty_list():
 assert find_duplicates([]) == []

def test_multiple_duplicates():
 assert find_duplicates([2, 2, 3, 3, 4, 4]) == [2, 3, 4]

def test_negative_numbers():
 assert find_duplicates([-1, -2, -1, -3, -2]) == [-1, -2]
