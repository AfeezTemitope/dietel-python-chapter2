
age = int(input("Enter your age: "))
maximum_heart_rate = 220 - age

# Calculate the target heart rate range (50-85% of maximum heart rate)
target_minimum = 0.5 * maximum_heart_rate
target_maximum = 0.85 * maximum_heart_rate


print(f"Your maximum heart rate is {maximum_heart_rate} beats per minute.")
print(f"Your target heart rate range is {target_minimum:.0f} to {target_maximum:.0f} beats per minute.")
