principal_amount = float(input('value for principal amount:'))
monthly_interest_rate = float(input('value for annual interest rate:'))
duration_of_loan = int(input('duration for loan in years:'))


number_of_month = (duration_of_loan * 12) 
rate = (monthly_interest_rate / 12) / 100
numerator = rate * principal_amount * (1 + rate) ** number_of_month
denominator = ((1 + rate) ** number_of_month ) - 1
monthly_payment = ( numerator / denominator)

print(f'Your monthly payment is ${monthly_payment:,.2f}')