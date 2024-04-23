print("Exercise 3.10")

("The pricipal amount is = $1000")
principal = int(input("Enter pricipal amount: "))
rate = int(input("Enter Annual rate of return:"))
calrate = rate / 100
interest = 0
index = 1
print("Years\t Amount")
print()
for numbers in range(30):
	interest = principal * calrate
	totalamount = principal + interest
	print(f"year{index}\t {principal:.2f}")
	principal = totalamount
	index += 1