from Code.Find_Missing_Number import find_missing_number

def test_missing_middle_number():
  assert find_missing_number([1, 2, 4, 5]) == 3

def test_missing_first_number():
  assert find_missing_number([2, 3, 4, 5]) == 1

def test_missing_last_number():
  assert find_missing_number([1, 2, 3, 4]) == 5

def test_missing_number_from_longer_list():
  assert find_missing_number([1, 2, 3, 5, 6, 7]) == 4

def test_single_number_missing():
  assert find_missing_number([]) == 1
