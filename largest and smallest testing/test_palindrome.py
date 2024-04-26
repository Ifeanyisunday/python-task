from palindrome import palindrome

def test_palindrome():
	assert palindrome("12121") == True
	assert palindrome("dad") == True
	assert palindrome("12123") == False
	assert palindrome("take") == False
	assert palindrome(" dad ") == True
	assert palindrome("12141") == False
	assert palindrome("334556") == False
	