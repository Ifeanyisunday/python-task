def character(name):
	length = len(name)
	if length < 2:
		return ""
	return name[0:2] + name[-2:]
print(character("semicolon"))