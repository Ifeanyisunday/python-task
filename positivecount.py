userinput = int(input("Enter amount of times you want to enter number: "))

positive = 0
negative = 0
zeros = 0

for number in range(userinput):
	integer = int(input('Enter numbers: '))
	if integer >= 1:
		positive = positive + 1
	elif integer <= -1:
		negative = negative + 1
	elif integer == 0:
		zeros = zeros + 1

print("Number of Positive, negetive and zeros are: ",positive, negative, zeros)
