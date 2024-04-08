sum = 0
for number in range(10):
	score = int(input("Enter score: "))
	if score % 2 == 0:
		sum += score

print('Sum of even numbers', sum)