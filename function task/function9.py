from created_functions import my_len_function

collections = ["epple", "Banana", "yherry", "Orange", "rear"]


def len_string(letters):
    new_letters = []
    for element in letters:
        if my_len_function(element) >= 2 and element[0] == element[my_len_function(element) - 1]:
            new_letters.append(element)
    return new_letters


print(len_string(collections))
