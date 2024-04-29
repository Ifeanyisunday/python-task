from functionroasted5 import remove_odd_index

def test_remove_odd_indexpass():
	assert remove_odd_index("abcdef") == "ace"
	assert remove_odd_index("python") == "pto"
	assert remove_odd_index("programming") == "pormig"
	assert remove_odd_index("aaaaaa") == "aaa"
	assert remove_odd_index("abcdef") == "ace"
	assert remove_odd_index("a1b2c3") == "abc"
	assert remove_odd_index("python3") == "pto3"
	assert remove_odd_index("aaaaaaa") == "aaaa"
	assert remove_odd_index("semicolon20") == "smcln0"
	assert remove_odd_index("aaaa") == "aa"
	assert remove_odd_index("") == ""
	
	


	