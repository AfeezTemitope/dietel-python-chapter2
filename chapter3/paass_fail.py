passed = 0
failed = 0

while True:
    try:
        result = int(input("Enter number between 1 or 2 (or -1 to quit): "))
        if result == 1:
            passed += 1
        elif result == 2:
            failed += 1
        elif result == -1:
            break
        else:
            print("Invalid input. Enter a valid integer (1, 2, or -1).")
            continue

    except ValueError:
        print("Invalid input. Enter a valid number 1, 2, or -1.")

print(f"Number of students passed: {passed}")
print(f"Number of students failed: {failed}")

if passed > 8: 
    print("Bonus to instructor!")
