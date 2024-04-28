def length_of_a_string(number):
	length = 0
	for char in number:
		length += 1
	return length

def length_of_a_string(sting):
	result = ''
	length = 0
	for char in sting:
		length += 1
	return length

	if length < 2:
		return result

	for i in range(2):
		result += sting[i]
	for i in range(length - 2, length):
		result += sting[i]


	return result

def adding_letters(suffix):
	length = 0
	for char in sting:
		length += 1

	if length < 3:
		return suffix

	ending_with_ing = False
	if lenght >= 3 and ing[length - 3] == 'i' and ing[length -2] == 'n' and ing[length -1] == 'g'
		ending_with_ing = True
	if ending_with_ing:
		suffix += "ly"
	else:
		suffix += 'ing'
	return suffix

def longest_word(wordings):
	longest =''
	longest_length = 0

	for word in wordings:
		length = 0
		for char in word:
			length += 1

		if length > longest_length:
			longest = word
			longest_length = length
	return longest, longest_length

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
