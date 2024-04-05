miltipleoffour = 1
miltipleofeight = 1
sum_multiple_four = 0
sum_multiple_eight = 0

for multiples in range(5):
	miltipleoffour = miltipleoffour * 4
	sum_multiple_four = sum_multiple_four + miltipleoffour 


for multiples in range(5):
	miltipleofeight = miltipleofeight * 8
	sum_multiple_eight = sum_multiple_eight + miltipleofeight

sum_total = sum_multiple_four + sum_multiple_eight

print(sum_total)