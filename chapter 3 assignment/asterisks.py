print("Exercise 3.17")

for number in range(10):
	print()
	for index in range(number):
		print("*", end = " ")

for number in range(10, 0, -1):
	print()
	for index in range(0, number):
		print("*", end = " ")

for number in range(10, 10, -1):
	print()
	for index in range(number, 0, -1):
		print()