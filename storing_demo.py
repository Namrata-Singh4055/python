

loan = int(input("Enter the cost of the loan: "))
rate = int(input("Enter the interest rate of the loan: "))
years = int(input("Enter the number of years for the loan: "))

payment = (loan*(rate*(1+rate)*years))/((1+rate)*years-1)

print(payment)

