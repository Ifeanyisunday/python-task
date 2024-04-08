prompt = int(input("How many numbers should be entered: "))

sum = 0

for count in range(prompt):
	number = int(input("Enter number: "))
	sum = sum + number
print(sum)
	
	