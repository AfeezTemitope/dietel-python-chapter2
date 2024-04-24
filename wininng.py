import random

ACTUAL_NUMBER = random.randrange(1, 10)

userInput = 0
while ACTUAL_NUMBER != userInput:
	userInput = int(input("Enter a number between (1 - 10):  "))


	if userInput == ACTUAL_NUMBER:
		print("You guessed correctly", ACTUAL_NUMBER)
		break
	else:
		print("Try again!")
