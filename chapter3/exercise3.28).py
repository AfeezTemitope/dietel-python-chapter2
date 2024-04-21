import statistics
n = int(input("Enter the number of elements: "))
values = []
for i in range(n):
    num = int(input(f"Enter number {i+1}: ",))
    values.append(num)

mean = statistics.mean(values)
print(f"The mean value is {mean}")

median = statistics.median(values)
print(f"The median value is {median}")

mode = statistics.mode(values)
print(f"The mode is {mode}")
