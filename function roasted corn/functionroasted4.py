def words(namelist):
	largest = 0
	list = []
	for i in range(7):
		list[i] = len(namelist[i])
	return list
print(words(['welcome', 'out', 'weather', 'mobile', 'breakfast', 'journey']))