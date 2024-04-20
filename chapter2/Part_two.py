
customer_name = input("Please enter Customer Name: ")
num_items = int(input("Please enter number of items purchased: "))
discount = float(input("Please Enter percentage discount: "))

total_cost = 0
CONSTANT_VALUE = 200


for i in range(1, num_items + 1):
	cost = float(input(f"Please Enter cost for item {i}: "))
	total_cost += cost

discounted_cost = total_cost - (total_cost * discount / 100)


print(f"Customer Name: {customer_name}")
print(f"Number of items bought: {num_items}")
print(f"Percentage discount: {discount}")
print(f"Original cost: {total_cost:.2f}")
print("Thanks for your patronage!")

if total_cost >= CONSTANT_VALUE:
	print(f"Discounted cost: {discounted_cost:.2f} (Discount applied)")    
else:
	print(f"NO DISCOUNT APPLIED")   


