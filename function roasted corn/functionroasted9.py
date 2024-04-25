def squared_list(numbers):
	squarenumbers = []
	square = 0
	for i in numbers:
		square = i ** 2 
		squarenumbers.append(square)
	return squarenumbers
numbers = [2, 3, 4, 5, 7]
print(squared_list(numbers))		