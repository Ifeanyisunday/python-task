number = int(input("Enter number: "))
fixednumber = number

factorial = 1
for fac in range(number):
	factorial = factorial * number
	number = number - 1
	
print("Factorial of ", fixednumber,"! is = ", factorial)