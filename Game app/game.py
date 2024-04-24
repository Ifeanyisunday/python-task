print("Welcome to Random game")
print("")
WINNING_NUMBER = 4
for number in range(3):
	guess_number = int(input("Enter number form 1 - 10: "))
	print("")
	while guess_number > 10:
		print("invalid number try again")
		guess_number = int(input("Enter number form 1 - 10: "))
	while guess_number < 1:
		print("invalid number try again")
		guess_number = int(input("Enter number form 1 - 10: "))
	if guess_number == WINNING_NUMBER:
		print("Yess!! congratulations you won")
		break
