number_1 = float(input("Enter the first number: "))
number_2 = float(input("Enter the second number: "))
number_3 = float(input("Enter the third number: "))

minimum_number = min(number_1, number_2, number_3)
maximum_number = max(number_1, number_2, number_3)
middle_number = number_1 + number_2 + number_3 - minimum_number - maximum_number


print(f"The numbers in increasing order: {minimum_number}, {middle_number}, {maximum_number}")
