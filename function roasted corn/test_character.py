from functionroasted2 import character

def test_character():
	assert character("grace") == "grce"
	assert character("pencil") == "peil"
	assert character("may") == "maay"
	assert character("a") == "" 
	assert character("python") == "pyon"
	assert character("hi") == "hihi" 
	assert character("hello world") == "held"  