print("Exercise 3.7")

print(F"number\tsquare\tcube")
for numbers in range(6):
	print(f'{numbers:>6}{numbers ** 2:>8}{numbers ** 3:>6}')