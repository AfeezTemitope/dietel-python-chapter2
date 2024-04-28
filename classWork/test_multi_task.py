from multi_task import largest_of_three,minimum

def test_largest_of_three():
	assert largest_of_three(1, 2, 3) == 3, "Test Case 1 Failed"
	assert largest_of_three(3, 2, 1) == 3, "Test Case 2 Failed"
	assert largest_of_three(1, 3, 2) == 3, "Test Case 3 Failed"
	assert largest_of_three(0, -1, -2) == 0, "Test Case 4 Failed"
	assert largest_of_three(-1, -1, -1) == -1, "Test Case 5 Failed"

def test_minimum():
	assert minimum([1, 2, 3]) == 1, "Test Case 1 Failed"
	assert minimum([3, 2, 1]) == 1, "Test Case 2 Failed"
	assert minimum([1, 3, 2]) == 1, "Test Case 3 Failed"
	assert minimum([0, -1, -2]) == -2, "Test Case 4 Failed"
	assert minimum([-1, -1, -1]) == -1, "Test Case 5 Failed"
	assert minimum([]) == None, "Test Case 6 Failed"
	assert minimum([5, 5, 5, 2, 5, 5, 5]) == 2, "Test Case 7 Failed"



