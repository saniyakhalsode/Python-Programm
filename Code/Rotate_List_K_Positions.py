def rotate_list(numbers, k):
    if not numbers:
        return []

    n = len(numbers)
    k = k % n

    return numbers[-k:] + numbers[:-k] if k != 0 else numbers.copy()


numbers = [1, 2, 3, 4, 5]
k = 2

result = rotate_list(numbers, k)

print("Original List:", numbers)
print("Rotated List:", result)