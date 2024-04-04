print("Welcome to E-store: \n")
name = input("Please enter customer name: \n")
number_of_item = int(input("please enter number of item purchased: \n"))

discount = int(input("please enter percentage discount: \n"))

original_cost = 0
counter = 0

while counter < number_of_item:
	cost = int(input("please enter cost of item:\n"))
	original_cost += cost
	counter += 1
	

print('')
print("Customer name: ", name)
print("Original cost:", original_cost)
discount_percent = original_cost * discount / 100
discount_cost = original_cost - discount_percent

if original_cost >= 200:
	print("Discounted cost:", discount_cost, "Discount applied")
elif original_cost < 200: 
	print("Discount cost: 0(No Discount applied)")

 	
	
	
	



