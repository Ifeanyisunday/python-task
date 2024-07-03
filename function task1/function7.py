from function1 import collection_of_number
from created_functions import my_len_function


def largest():
    large = 0
    for index in range(0, my_len_function(collection_of_number())):
        if collection_of_number()[index] > large:
            large = collection_of_number()[index]
    return large
print(largest())