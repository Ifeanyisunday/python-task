from function1 import collection_of_number
from function_task2.created_functions import my_len_function

number_collection = [collection_of_number()]


def smallest(numbers):
    small = numbers[0]
    for index in range(0, my_len_function(numbers)):
        if numbers[index] < small:
            small = numbers[index]
    return small

