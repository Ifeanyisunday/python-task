print("Exercise 3.11")

gallons = 0
miles = 0
cal = 0
total = 0
count = 0
while gallons != -1:
	gallons = float(input("Enter the gallons used: "))
	if gallons == -1:
		break
	miles = int(input("Enter the miles driven: "))
	
	cal = miles / gallons
	total += cal
	print(f"The miles/gallons for this tank was {cal:.6f}")
	count += 1
average = total / count

print("The overall average miles/gallon was ", average)