def character(name):
	length = len(name)
	if length > 2:
		if name[-3:] == "ing":
			return name + "ly"
		else:
			return name + "ing" 
print(character("semicolon"))