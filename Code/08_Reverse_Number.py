
def reverse_number(num):
    sign = -1 if num < 0 else 1
    num = abs(num)
    reversed_num = 0

    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10

    return sign * reversed_num


def main():
    num = int(input("Enter a number: "))
    result = reverse_number(num)
    print("Reversed number:", result)


if __name__ == "__main__":
    main()

