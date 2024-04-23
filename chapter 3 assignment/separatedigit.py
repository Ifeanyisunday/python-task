print("Exercise 3.8")

input1 = int(input("enter digits: "))
input2 = 0
digit = 0
divisor = 10000
count = 10

for numbers in range(5):
	input2 = input1 // divisor
	print(input2,",", end = " ")
	digit = input1 % divisor
	input1 = digit
	counter = divisor // count
	divisor = counter

	