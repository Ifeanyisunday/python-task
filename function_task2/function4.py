from function1 import collection_of_number
from function_task2.created_functions import my_len_function

number_collection = [collection_of_number()]


def sum_of_odd_index(numbers):
    total = 0
    for index in range(0, my_len_function(numbers)):
        if index % 2 != 0:
            total = total + numbers[index]
    return total

