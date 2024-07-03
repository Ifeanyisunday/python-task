numbers1 = {6, 4, 3, 4, 8}
numbers2 = {2, 3, 5, 4, 5, 6, 7}


def union_of_two_sets(num1, num2):
    union_numbers = num1.union(num2)
    return union_numbers


print(union_of_two_sets(numbers1, numbers2))
