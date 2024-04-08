eventotal = 0
numberofevennumbers = 0
for number in range(10):
	score = int(input("Enter score: "))
	if score % 2 == 0:
		eventotal += score
		numberofevennumbers += 1

average = eventotal / numberofevennumbers

print("the sum of the even numbers is ", eventotal)
print("the average of the even numbers is ", average)

