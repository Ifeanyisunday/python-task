<<<<<<< HEAD
print("")
principal = int(input("Enter the principal amount: "))
print("")
assume_interest = int(input("Enter the annual interest rate: "))
print("")
duration = int(input("Enter the duration in years: "))
print("")

annual_interest = assume_interest / 100
monthly_rate = annual_interest / 12
number_of_months_in_years = duration * 12

monthly_exponent = (1 + monthly_rate)**number_of_months_in_years

monthly_payment = principal * (monthly_rate * monthly_exponent) / (monthly_exponent - 1)


=======
print("")
principal = int(input("Enter the principal amount: "))
print("")
assume_interest = int(input("Enter the annual interest rate: "))
print("")
duration = int(input("Enter the duration in years: "))
print("")

annual_interest = assume_interest / 100
monthly_rate = annual_interest / 12
number_of_months_in_years = duration * 12

monthly_exponent = (1 + monthly_rate)**number_of_months_in_years

monthly_payment = principal * (monthly_rate * monthly_exponent) / (monthly_exponent - 1)


>>>>>>> 37f5bb5d8452cb40f3a8f9fad63707cca77afc44
print("Your monthly payment is $" + round(monthly_payment, 2))