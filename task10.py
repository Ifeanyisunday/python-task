sum = 0
noofvalidscore = 0

for number in range(10):
	score = int(input("Enter score: "))
	if score <= 100:
		sum += score
		noofvalidscore += 1

average = sum / noofvalidscore

print("the average is ", average)
