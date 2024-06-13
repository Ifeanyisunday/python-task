new_set = {3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5}


def find_largest_and_smallest(numbers):
    largest = 0
    for element in numbers:
        if element > largest:
            largest = element

    smallest = 0
    for element in numbers:
        if element > smallest:
            smallest = element
            break
    for element in numbers:
        if element < smallest:
            smallest = element
    return largest, smallest


print(find_largest_and_smallest(new_set))
