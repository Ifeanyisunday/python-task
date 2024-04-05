print("a\t", "b\t", "pow(a, b)")

a = 1
b = 2
for number in range(5):
	print(f"{a}\t {b}\t {a ** b}")
	a = a + 1
	b = b + 1