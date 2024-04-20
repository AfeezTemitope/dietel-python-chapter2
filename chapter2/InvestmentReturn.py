amount_invested = int(input("enter value for the original amount invested\n"))
number_of_years = int(input("enter value for number of years\n"))
annual_rate_of_return = 0.07
amount_deposit = amount_invested * (1 + annual_rate_of_return) ** number_of_years 
print( "amount deposit for ", number_of_years)
print( "amount deposit is", amount_deposit )
