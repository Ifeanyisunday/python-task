def palindrome(letter):
	length = len(letter)
	letter2 = ""
	for i in range(length-1, -1, -1):
		letter2 += letter[i]
	if letter2 == letter:
		return True
	else:
		return False