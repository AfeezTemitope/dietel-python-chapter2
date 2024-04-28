from multi_task import largest_of_three,minimum

def test_largest_of_three():
	assert largest_of_three(1, 2, 3) == 3
	assert largest_of_three(3, 2, 1) == 3
	assert largest_of_three(1, 3, 2) == 3
	assert largest_of_three(0, -1, -2) == 0
	assert largest_of_three(-1, -1, -1) == -1

def test_minimum():
	assert minimum([1, 2, 3]) == 1
	assert minimum([3, 2, 1]) == 1
	assert minimum([1, 3, 2]) == 1
	assert minimum([0, -1, -2]) == -2
	assert minimum([-1, -1, -1]) == -1
	assert minimum([]) == None
	assert minimum([5, 5, 5, 2, 5, 5, 5]) == 2



