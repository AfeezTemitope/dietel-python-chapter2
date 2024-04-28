from roatsed_corn import minimum,find_sum_of_squares_in_a_list

def test_find_minimum_():
	assert minimum([2,3,45,6,77,6,55,4,34]) == 2
	assert minimum([2,3,45,6,77,6,55,4,34]) != 77

def test_find_sum():
	assert find_sum_of_squares_in_a_list([1, 2, 3]) == 14
	assert find_sum_of_squares_in_a_list([-1, -2, -3]) == 14
	assert find_sum_of_squares_in_a_list([0, 0, 0]) == 0
	assert find_sum_of_squares_in_a_list([1, -1, 1, -1]) == 4
	assert find_sum_of_squares_in_a_list([5]) == 25
	assert find_sum_of_squares_in_a_list([]) == 0
	assert find_sum_of_squares_in_a_list([1, 2, 3, 4, 5]) != 66

