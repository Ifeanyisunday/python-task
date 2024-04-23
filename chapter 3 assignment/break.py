print("Exercise 3.22")

for i in range(2):
	value = int(input('Enter an integer (-1 to break): '))
	if value > 0:
		print('You entered:', value)
	else:
		print('The loop terminated')
		break