
def calculate_factorial(num):
    if num < 0:
        return "Factorial is not defined for negative numbers"

    factorial = 1

    for i in range(1, num + 1):
        factorial *= i

    return factorial


def main():
    num = int(input("Enter a number: "))
    result = calculate_factorial(num)
    print("Factorial:", result)


if __name__ == "__main__":
    main()
