def find_intersection(set1, set2):
    result = set()

    for element in set1:
        if element in set2:
            result.add(element)

    return result


set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

result = find_intersection(set1, set2)

print("First Set:", set1)
print("Second Set:", set2)
print("Intersection:", result)