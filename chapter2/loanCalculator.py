amount = int(input(" Enter loan amount: "))
duration_of_loan = int(input(" Enter number of years for loan "))


for i in range (duration_of_loan):
	RATE = 20 / 100	
	interest_on_loan =  RATE * amount 
	amount += interest_on_loan
	
	
	print(f" onigbese see your loan for year {i + 1} :  ${amount:,.2f}")