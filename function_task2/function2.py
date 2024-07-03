from function1 import collection_of_number

numbers_collections = [collection_of_number()]


def find_length_without_len_function(numbers):
    counter = 0
    for number in numbers:
        counter += 1
    return counter


print(find_length_without_len_function(numbers_collections))
