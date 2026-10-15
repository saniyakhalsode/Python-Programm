def find_missing_number(numbers):
    n = len(numbers) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)

    return expected_sum - actual_sum

def main():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))


    result = find_missing_number(numbers)

    print("Missing number:", result)


if __name__ == "__main__":
  main()
