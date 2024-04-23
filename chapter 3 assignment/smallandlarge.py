print("Exercise 3.8")

sum = 0
product = 1
smallest = 0
largest = 0
user_input = int(input("Enter first integer: "))
for input in range(4):
	user_input = int(input("Enter first integer: "))
	smallest = user_input
	if user_input > largest:
		largest = user_input
	if user_input < smallest:
		smallest = user_input
	sum += user_input
	product *= user_input
	
##user_input2 = int(input("Enter second integer: "))
##user_input3 = int(input("Enter third integer: "))
print("")
average = sum / 4

print("The sum of the 4 inputs is ",sum)
print("The average of the 4 inputs is ",average)
print("The product of the 4 inputs is ",product)
print("The smallest of the 4 inputs is ",smallest)
print("The largest of the 4 inputs is ",largest)