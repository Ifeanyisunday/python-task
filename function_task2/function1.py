import random


def collection_of_number():
    ten_numbers = []
    random.seed(50)
    for numbers in range(10):
        rand_numbers = random.randint(1, 50)
        ten_numbers.append(rand_numbers)

    return ten_numbers
