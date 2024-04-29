from functionroasted6 import minimum

def test_minimum():
	assert minimum([2, 14, 1, 4]) == 1
	assert minimum([3, 1, 4, 1, 5, 9, 1]) == 1
	assert minimum([-5, -10, -2]) == -10
	assert minimum([2, 4, 6, 8, 2]) == 2
	assert minimum([1.5, 2.3, 0.7, 0.7]) == 0.7
	assert minimum([3, 3, 3, 3, 3]) == 3
	assert minimum([10**5, -10**6]) == -10**6