def sum_list(numbers):
	sum = 0
	squarenumbers = []
	square = 0
	for i in numbers:
		square = i ** 2 
		squarenumbers.append(square)
	
	for i in squarenumbers:
		sum += i 
	return sum
numbers = [2, 3, 4, 5, 7]
print(sum_list(numbers))


		