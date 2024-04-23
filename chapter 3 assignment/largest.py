print("Exercise 3.16")


largest1 = 0
largest2 = 0

for number in range(10):
	user = int(input("Enter number: "))
	if user > largest1:
		largest1 = user
	if user == largest1:
		continue
	if user > largest2:
		largest2 = user
		


print(largest1, largest2)
	