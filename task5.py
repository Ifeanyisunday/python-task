eventotal = 0
for number in range(10):
	score = int(input("Enter score: "))
	if score % 2 == 0:
		eventotal += score

print('Sum of even numbers', eventotal)