sum = 0

for number in range(10):
	score = int(input("Enter score: "))
	if score < 100:
		sum += score

print("the sum of the even numbers is ", sum)
