print("Exercise 3.13")


input1 = int(input("enter digits: "))
index = 1
factorial = 1
for numbers in range(input1):
	factorial *= index
	index += 1
print(factorial)
