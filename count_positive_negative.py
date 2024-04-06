positive_count = 0
negative_count = 0
zero_count = 0

    
while True:
        try:
            num = int(input("Enter a number (0 to exit): "))
            if num == 0:
                break
            elif num > 0:
                positive_count += 1
            else:
                negative_count += 1
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    
print(f"Positive numbers: {positive_count}")
print(f"Negative numbers: {negative_count}")
print(f"Zeroes: {zero_count}")


