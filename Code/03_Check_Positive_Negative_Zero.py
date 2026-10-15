
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"


def main():
    num = int(input("Enter a number: "))
    result = check_number(num)
    print("The number is", result)


if __name__ == "__main__":
    main()
