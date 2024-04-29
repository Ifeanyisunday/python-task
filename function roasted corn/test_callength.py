from functionroasted1 import callength

def test_callength():
	assert callength("grace") == 5
	assert callength("pencil") == 6
	assert callength("may") == 3
	assert callength("semicolon") == 9
	assert callength("programming") == 11
	assert callength("jump") == 4
	assert callength("love") == 4