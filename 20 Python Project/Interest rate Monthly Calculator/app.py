# Collect the necessary inputs: principal, annual interest rate, years
# calculate the monthly payment 
# output

def main():
    print("This is a monthly loan calculator")
    print("")

    principal = float(input("Supply loan amount: "))
    apr = float(input("Supply Annual interest rate amount: "))
    years =int (input("supply amount of years: "))

    monthlyInterestRate = apr/1200
    amountOfMonths = years * 12
    monthlyPayment = principal * monthlyInterestRate / (1 - (1 + monthlyInterestRate) ** (-amountOfMonths))

    print("Monthly payment is : %.2f" %monthlyPayment)

main()