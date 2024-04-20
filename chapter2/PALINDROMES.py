print("**************")
print("WELCOME TO PALINDROMES")
print("**************")

user_input = int(input("enter a number between 100 - 9999"))

thousand =  user_input // 1000
hundred = (user_input // 100) % 10
ten = (user_input // 10) % 10
unit = user_input % 10

sum = thousand + hundred + ten + unit

print("**************")
print(f"sum of palindromes is {sum}")
print("**************")

