from function1 import collection_of_number


def find_length_without_len_function():
    counter = 0
    for number in collection_of_number():
        counter += 1
    return counter


print(find_length_without_len_function())
