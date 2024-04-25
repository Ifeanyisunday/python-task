def remove_odd_index(name):
	for i in range(len(name)):
		replace = ""
		if i % 2 == 0:
			replace += name[i]
	return replace

print(remove_odd_index("semicolon"))