sum_of_muiltiple = 0

for numbers in range(1, 20_001):
	if numbers % 10 == 0:
		sum_of_muiltiple += numbers

print("The sum of multiples of 10 from 1 - 20,000 is ",sum_of_muiltiple)
	