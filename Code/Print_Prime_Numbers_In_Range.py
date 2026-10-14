
def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


def print_prime_numbers(start, end):
    prime_numbers = []

    for num in range(start, end + 1):
        if is_prime(num):
            prime_numbers.append(num)

    return prime_numbers


def main():
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))

    result = print_prime_numbers(start, end)

    print("Prime numbers:", result)


if __name__ == "__main__":
    main()
