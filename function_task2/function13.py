numbers1 = {6, 4, 3, 4, 8}
numbers2 = {2, 3, 5, 4, 5, 6, 7}


def subset_of_two_sets(num1, num2):
    subset_numbers = num1.issubset(num2)
    if subset_numbers:
        return True
    else:
        return False
