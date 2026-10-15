
def generate_fibonacci(n):
    if n <= 0:
        return []

    series = []
    a, b = 0, 1

    for i in range(n):
        series.append(a)
        a, b = b, a + b

    return series


def main():
    n = int(input("Enter the number of terms: "))
    result = generate_fibonacci(n)
    print("Fibonacci Series:", result)


if __name__ == "__main__":
    main()
