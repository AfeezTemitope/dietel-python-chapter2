def add_numbers():
    numbers = []

    while True:
        num = input("Enter a number (or 'stop' to finish): ")
        if num.lower() == 'stop':
            break
        numbers.append(int(num))

    return sum(numbers)


total = add_numbers()
print("The sum of the numbers is", total)
