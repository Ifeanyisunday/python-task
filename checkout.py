customername = str(input("what is the customer's name: "))

storeitem = []
storequantity = []
totalprice = []
total = float(0)

def items():
	print(item = str(input("what did the user buy?: ")))
	storeitem += item	
	print(quantity = int(input("How many pieces?: ")))
	print(price = float(input("how many units?: ")))
	total += price * quantity

items()
userinput = input("Do you want to continue? (yes/no)")		

while userinput == "yes":
	items()

