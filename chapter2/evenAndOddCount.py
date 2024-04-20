
badAfeez = [22, 33, 45, 3, 22, 5, 67, 88, 87, 98, 2]
evenCount, oddCount = 0, 0

for num in badAfeez:
        evenCount += 1 if num % 2 == 0 else 0
        oddCount += 1 if num % 2 != 0 else 0

print(f"Count of even numbers: {evenCount}\nCount of odd numbers: {oddCount}")

