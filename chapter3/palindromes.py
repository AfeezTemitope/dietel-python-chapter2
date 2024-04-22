number = int(input("enter five digit integer  "))
original_number = number
new_number = 0

while number > 0:
    digit = number % 10
    new_number = new_number * 10 + digit
    number = number // 10

print(f"{original_number} is a palindrome ") if original_number == new_number else print(f"{original_number } is not a palindrome.")
