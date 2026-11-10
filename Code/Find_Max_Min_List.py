def find_max_min(numbers):
    if len(numbers) == 0:
        raise ValueError("List cannot be empty")

    maximum = numbers[0]
    minimum = numbers[0]

    for num in numbers:
        if num > maximum:
            maximum = num

        if num < minimum:
            minimum = num

    return maximum, minimum


numbers = [10, 25, 5, 40, 15]

maximum, minimum = find_max_min(numbers)

print("Maximum number:", maximum)
print("Minimum number:", minimum)