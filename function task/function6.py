from function1 import collection_of_number
from created_functions import my_len_function


def average():
    total = 0
    for index in range(0, my_len_function(collection_of_number())):
        total = total + collection_of_number()[index]
    return total / my_len_function(collection_of_number())


print(average())
