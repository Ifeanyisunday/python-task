sample_input = int(input("Sample input: "))

for numbers in range(sample_input, 0, -1):
	for index in range(numbers, 0, -1):
		print(index, end = " ")
	print()