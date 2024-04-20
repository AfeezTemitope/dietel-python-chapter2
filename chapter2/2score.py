grade = int(input("enter score "))

if grade > 100:
	print('you are a criminal, you should get arrested')
elif grade >= 80 and grade <= 100:
	print(f"you score {grade} and your grade is A")
elif grade >=65 and grade < 80:
	print(f"you score {grade} and your grade is B")
elif grade >=50 and grade < 65:
	print(f"you score {grade} and your grade is C")
elif grade >=40 and grade < 50:
	print(f"you score {grade} and your grade is D")
else:
	print('you fail')
	

