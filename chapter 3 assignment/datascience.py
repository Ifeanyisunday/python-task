import statistics
print("Exercise 3.28")

numbers = 0

calmean = 0
calmedian = 0
list = []
for number in range(10):
	numbers = int(input("Enter number: "))
	list.append(numbers)
	calmean += numbers
	if number == 4:
		calmedian += numbers
	elif number == 5:
		calmedian += numbers

	

mean = calmean / 10
median = calmedian / 2
mode = statistics.mode(list)
print("The mean is ", mean)
print("The median is ", median)
print("The mode is ", mode)		
	