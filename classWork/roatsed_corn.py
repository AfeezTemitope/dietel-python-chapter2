def minimum(number):
	if not number:
		return None
	minimum = number[0]
	for num in number:
		if num < minimum:
			minimum = num
	return minimum

def find_sum_of_squares_in_a_list(lst):
	return sum(x**2 for x in lst)

def find_square(lst):
	return x**2 for x in lst
