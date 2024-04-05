userinput = int(input("Enter amount of times you want to enter number: "))

positive = 0
negative = 0
zeros = 0

for number in range(userinput):
	integer = int(input('Enter numbers: '))
	if userinput >= 1:
		positive = positive + 1
	elif userinput <= -1:
		negative = negative + 1
	else userinput == 0:
		zeros = zeros + 1

print("Number of Positive, negetive and zeros are: ",positive, negative,zeros)
		
	