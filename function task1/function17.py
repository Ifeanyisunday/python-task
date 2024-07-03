from created_functions import my_len_function


def add_to_tuple():
    new_tuple = ()
    for i in range(1, 21):
        new_tuple = new_tuple + (i,)
    return new_tuple


def add_odd_index():
    add_to_tuple()
    sum = 0
    for index in range(my_len_function(add_to_tuple())):
        if index % 2 != 0:
            sum = sum + add_to_tuple()[index]
    return sum


def add_even_index():
    add_to_tuple()
    sum = 0
    for index in range(my_len_function(add_to_tuple())):
        if index % 2 == 0:
            sum = sum + add_to_tuple()[index]
    return sum


def add_largest_and_smallest():
    add_to_tuple()
    largest = 0
    smallest = add_to_tuple()[0]
    sum_largest_and_smallest = 0
    for element in add_to_tuple():
        if element > largest:
            largest = element

    for element in add_to_tuple():
        if element < smallest:
            smallest = element

    sum_largest_and_smallest = largest + smallest
    return sum_largest_and_smallest


def unpack_tuple():
    add_to_tuple()
    sum = 0
    for index in range(my_len_function(add_to_tuple())):
        if index != 5:
            print(add_to_tuple()[index], " ", end="")
        else:
            break


print(add_odd_index())
print(add_even_index())
print(add_largest_and_smallest())
print(unpack_tuple())
