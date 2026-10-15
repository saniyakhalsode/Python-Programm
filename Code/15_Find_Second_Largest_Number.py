def find_second_largest(numbers):
    unique_numbers = list(set(numbers))


    if len(unique_numbers) < 2:
    
         return None

    unique_numbers.sort(reverse=True)
    return unique_numbers[1]

def main():
    numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

    result = find_second_largest(numbers)

    if result is None:
        print("Second largest number does not exist.")
    else:
        print("Second largest number:", result)

if __name__ == "__main__":
    main()
