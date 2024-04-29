from functionroasted7 import maximum

def test_maximum():
	assert maximum([2, 14, 1, 4]) == 14
	assert maximum([3, 1, 4, 1, 5, 9, 1]) == 9
	assert maximum([-5, -10, -2]) == 0
	assert maximum([2, 4, 6, 8, 2]) == 8
	assert maximum([1.5, 2.3, 0.7, 0.7]) == 2.3
	assert maximum([3, 3, 3, 3, 3]) == 3
	assert maximum([10**5, -10**6]) == 10**5