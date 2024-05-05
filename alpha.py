def counter(word):
	no_of_vowel = 0
	no_of_consonant = 0
	
	vowel = ["a", "e", "i", "o", "u"]
	consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "w", "x", "y", "z",]

	for index in vowel:
		if index in word:
			no_of_vowel += 1
	for index in consonants:
		if index in word:
			no_of_consonant += 1
	return f"Consonant {no_of_consonant} vowel {no_of_vowel}"

print(counter("intenational"))
					  