from function1 import collection_of_number
from function_task2.created_functions import my_len_function

number_collection = [collection_of_number()]


def sum_of_third_index(numbers):
    total = 1
    for index in range(0, my_len_function(numbers), +2):
        total = total * numbers[index]
    return total

