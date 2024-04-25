def minimum(numbers):
	minimum = numbers[0]
	for i in range(len(numbers)):
		if numbers[i] < minimum:
			minimum = numbers[i]
	return minimum
print(minimum([8, 4, 9, 2, 5, 7, 3]))		