customername = str(input("what is the customer's name: "))

storeitem = []
storequantity = []
totalprice = []
total = float(0)

def input():
	item = str(input("what did the user buy?: "))
	storeitem += item	
	quantity = int(input("How many pieces?: "))
	price = float(input("how many units?: "))
	total += price * quantity
		
while True:
	userinput = input("Do you want to continue? (yes/no)")
	if userinput.lower() in ["yes", "y"]:
		print("continuing....")
		break
	elif userinput.lower() in ["no", "n"]:
		print("Exiting...")
		break
	else:
		print("invalid input.please enter yes/no.")
	


