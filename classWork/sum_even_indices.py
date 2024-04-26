def sum_even_indices(array):
	return sum(array[::2])


numbers = [ 1,2,4,3,2,1,4,5,6,4,3,2,1]
total = sum_even_indices(numbers)
print(total)
