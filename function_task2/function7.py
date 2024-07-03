from function1 import collection_of_number
from function_task2.created_functions import my_len_function

number_collection = [collection_of_number()]


def largest(numbers):
    large = 0
    for index in range(0, my_len_function(numbers)):
        if numbers[index] > large:
            large = numbers[index]
    return large

