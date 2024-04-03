try:
	digit = int(input("enter  5 integer value"))

for digit.isdigit() and len(digit) == 5:
	print(digit, end="  ")
except ValueError:
	print("enter a valid 5 integer numbers")
