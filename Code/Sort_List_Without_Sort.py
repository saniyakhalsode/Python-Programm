def sort_list(numbers):

    new_list = numbers.copy()

    n = len(new_list)

    for i in range(n):
        for j in range(0, n - i - 1):

            if new_list[j] > new_list[j + 1]:

                new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]

    return new_list


if __name__ == "__main__":

    numbers = [5, 2, 8, 1, 3]

    result = sort_list(numbers)

    print("Original List:", numbers)
    print("Sorted List:", result)