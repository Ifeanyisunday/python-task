from function1 import collection_of_number
from created_functions import my_len_function


def sum_of_third_index():
    total = 1
    for index in range(0, my_len_function(collection_of_number()), +2):
        total = total * collection_of_number()[index]
    return total


print(sum_of_third_index())
