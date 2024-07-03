def sequential_collection():
    new_number1 = []
    new_numbers = []
    final_numbers = []
    for i in range(1, 16):
        new_numbers.append(i)
        new_numbers.append(i)
        new_number1.append(i)
    for element in new_number1:
        if element in new_numbers:
            final_numbers.append(element)
    return final_numbers


print(sequential_collection())
