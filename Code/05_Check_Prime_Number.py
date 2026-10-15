
def check_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


def main():
    num = int(input("Enter a number: "))

    if check_prime(num):
        print("The number is Prime")
    else:
        print("The number is Not Prime")


if __name__ == "__main__":
    main()

