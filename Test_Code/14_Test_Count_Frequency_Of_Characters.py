from collections import Counter


def count_characters(text):
  # Core logic function
  return Counter(text)


# Define test cases: (input_string, expected_frequency_dictionary)
test_cases = [
    ("hello", Counter({"h": 1, "e": 1, "l": 2, "o": 1})),
    ("aab", Counter({"a": 2, "b": 1})),
    ("racecar", Counter({"r": 2, "a": 2, "c": 2, "e": 1})),
    ("   ", Counter({" ": 3})),  # Only spaces
    ("", Counter({})),  # Empty string
    ("112233", Counter({"1": 2, "2": 2, "3": 2})),  # Numbers
]

# Run tests automatically
print("--- Running Tests ---")
for i, (test_input, expected) in enumerate(test_cases, 1):
  result = count_characters(test_input)
  status = "PASS" if result == expected else "FAIL"
  print(
      f"Test {i}: Input '{test_input}' -> Got {dict(result)} | Expected"
      f" {dict(expected)} [{status}]"
  )
