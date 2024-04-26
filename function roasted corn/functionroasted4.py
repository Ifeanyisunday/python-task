def words(namelist):
	longest = 0
	longest_word = ""
	for i in namelist:
		if len(i) > longest:
			longest = len(i)
			longest_word = i
			
	return longest_word, longest
print(words(['welcome', 'out', 'weather', 'mobile', 'breakfast', 'journey']))