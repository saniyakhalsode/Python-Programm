def find_duplicates(numbers):
 duplicates = []

 for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

 return duplicates

def main():
 numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

 result = find_duplicates(numbers)

 print("Duplicate elements:", result)

if __name__ == "__main__":
 main()
