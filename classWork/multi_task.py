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













		