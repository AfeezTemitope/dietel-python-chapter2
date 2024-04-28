def largest_of_three(num1, num2, num3):
	if num1 >= num2 and num1 >= num3:
		return num1
	elif num2 >= num1 and num2 >= num3:
		return num2
	else:
		return num3



def minimum(number):
	if not number:
		return None
	minimum = number[0]
	for num in number:
		if num < minimum:
			minimum = num
	return minimum


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











		