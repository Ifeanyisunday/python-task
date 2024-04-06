number = int(input("Enter number between 0 and 1000: "))

digit1 = number % 10
number2 = number // 10
digit2 = number2 % 10
number3 = number2 // 10
digit3 = number3 % 10

sumdigits = digit1 + digit2 + digit3

print("The sum of the digits in", number, "is", sumdigits)