from function1 import collection_of_number
from created_functions import my_len_function


def sum_of_even_index():
    total = 0
    for index in range(0, my_len_function(collection_of_number())):
        if index % 2 == 0:
            total = total + collection_of_number()[index]
    return total


print(sum_of_even_index())
