from function_task2.function10 import sequential_collection
from function_task2.created_functions import my_len_function

number_collection = sequential_collection()


def add_element(numbers):
    total = 0
    for i in range(0, my_len_function(numbers), +2):
        total += numbers[i]
    return total

