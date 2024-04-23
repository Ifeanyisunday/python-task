
sum = 0
count = 0
product = 1
smallest = 0
largest = 0
digit = 0

for number in range(4):
	digit = int(input("Enter number: "))
	sum += digit
	product *= digit
	if digit > largest:
		largest = digit
	if digit < smallest:
		smallest = digit
	count += 1
	
average = sum / count

print("The sum is = ",sum)
print("The average is = ",average)
print("The product is = ",product)
print("The smallest is = ",smallest)
print("The largest is = ",largest)	