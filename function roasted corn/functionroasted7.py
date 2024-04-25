def maximum(numbers):
	maximum = 0
	for i in range(len(numbers)):
		if numbers[i] > maximum:
			maximum = numbers[i]
	return maximum
print(maximum([8, 4, 9, 2, 5, 7, 3]))		