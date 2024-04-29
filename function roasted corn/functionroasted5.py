def remove_odd_index(name):
	even = ""
	for i in range(len(name)):
		if i % 2 == 0:
			even += name[i]
		
	return even

print(remove_odd_index("semicolon"))