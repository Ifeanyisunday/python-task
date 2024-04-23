print("Exercise 3.1")

number = int(input("Enter number: "))
failure = 0
while number != 1 | number != 2:
	number = int(input("Enter number: "))
	if number == 1 | number == 2:
		break
		failure += 1

print(failure)