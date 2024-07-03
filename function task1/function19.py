from created_functions import my_len_function


def add_to_dictionary():
    my_dict = {}
    for index in range(1, 11):
        user_name = input("Enter name: ")
        user_age = int(input("Enter age: "))
        my_dict[user_name] = user_age
    return my_dict


def display_by_keys():
    my_dict = {}
    for index in range(1, 11):
        user_name = input("Enter name: ")
        user_age = int(input("Enter age: "))
        my_dict[user_name] = user_age
    return my_dict.keys()


def display_by_values():
    my_dict = {}
    for index in range(1, 11):
        user_name = input("Enter name: ")
        user_age = int(input("Enter age: "))
        my_dict[user_name] = user_age
    return my_dict.values()


def display_sum_of_all_ages():
    sum_age = 0
    display_by_values()
    for index in range(my_len_function(display_by_values())):
        sum_age += display_by_values()
    return sum_age


##print(add_to_dictionary())
print(display_by_keys())
print(display_by_values())
print(display_sum_of_all_ages())
