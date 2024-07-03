def collect_10_numbers():
    my_lst = []
    for index in range(10):
        user_input = int(input("Enter a number: "))
        if user_input not in my_lst:
            my_lst.append(user_input)
        else:
            print("Sorry, that number is already in list.")
    return my_lst


my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
my_set1 = {2, 4, 6, 8, 10}


def sum_collection(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum


def remove_item(numbers, digit):
    if digit in numbers:
        numbers.remove(digit)
        return numbers
    else:
        return "None"


def find_intersection(set1, set2):
    intersection = set1.intersection(set2)
    return intersection


##print(collect_10_numbers())
print(sum_collection(my_set))
print(remove_item(my_set, 10))
print(find_intersection(my_set, my_set1))
