def even_number():
	numbers = []
	for i in range(1,12,2):
		num = input("enter numbers ")
		numbers.append(int(num))
	return sum(numbers)


total = even_number()
print("the sum of the numbers is ", total)



