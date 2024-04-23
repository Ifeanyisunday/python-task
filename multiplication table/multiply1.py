count1 = 1
count2 = 1
multiply = 0
for number in range(12):
	for index in range(12):
		print(f"{count2:2d} x {count1:1d} = {count2 * count1:1d}\t",end="")
		count2 += 1
		if count2 > 12:
			count2 = 1
	print()
	count1 += 1
	

	