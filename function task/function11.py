from function10 import sequential_collection
from created_functions import my_len_function


def add_element():
    total = 0
    sequential_collection()
    for i in range(0, my_len_function(sequential_collection()), +2):
        total += sequential_collection()[i]
    return total


print(add_element())
