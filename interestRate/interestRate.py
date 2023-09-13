def month_InterestRate():
    try:
        print("This is a monthly interest payment")
        print("")

        principal = float(input("Enter the loan amount : "))
        apr = float(input("Enter the annual interest rate : "))
        years = int(input("Enter the number of years : "))

        monthly_interest_rate = apr / 1200
        months = years * 12

        monthly_payment = principal * monthly_interest_rate / (1-(1+monthly_interest_rate) ** (-months))
        print("Monthly payment for this loan is = ", round(monthly_payment,2))
        print("Monthly payment for this loan is = %.2f" % monthly_payment)
    except:
        print("Invalid Input!")

month_InterestRate()
