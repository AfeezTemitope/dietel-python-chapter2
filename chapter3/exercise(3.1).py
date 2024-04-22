total_miles = 0
total_gallon = 0
count = 0
while True:
    miles = int(input("enter drivers miles(-1 to end)"))
    if miles == -1:
        break     
    gallons = int(input(" enter gallon used"))
    total_miles += miles 
    total_gallon += gallons
    count += 1
    result = gallons / miles
    print("the miles/perGallon for this tank was ",result)
if count > 0:
        average = total_miles/ total_gallon
        print(f'the overall avaerage miles is {average}')