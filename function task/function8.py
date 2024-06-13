from function1 import collection_of_number
from created_functions import my_len_function


def smallest():
    small = collection_of_number()[0]
    for index in range(0, my_len_function(collection_of_number())):
        if collection_of_number()[index] < small:
            small = collection_of_number()[index]
    return small

print(smallest())