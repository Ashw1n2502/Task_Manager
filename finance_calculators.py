# Finance Calculator

import math

border = "-" * 100  
print(border)
print("investment - to calculate the amount of interest you'll earn on your investment")
print("   bond    - to calculate the amount you'll have to pay on a home loan")
print(border)
user_entry = input("Enter either 'investment' or 'bond' from the menu above to proceed : ").lower()

#Error message if user hasn't entered 'investment' or 'bond'
if user_entry != "investment" and user_entry != "bond" :
    print("You have not entered a valid input. Please try again.") 

#Calculating the total amount of money if the user inputs investment 
if user_entry == "investment" :
    deposit  = int(input("Please enter the amount of money you are depositing (in £) : "))
    rate     = int(input("Please enter the interest rate (in %) : "))
    time     = int(input("Please enter the number of years you plan on investing for : "))
    interest = input("Please enter if you would like simple or compound interest? : ").lower() 

    # Calculation of the total amount of money depending on the user's interest input
    if interest == "simple" :
        total_amount = int(deposit * (1 + (rate / 100) * time))
        print(f"Your total simple amount after {rate} years is : £ {total_amount}")

    elif interest == "compound" :
        total_amount = int(deposit * math.pow((1 + (rate / 100)), time))
        print(f"Your total compounded amount after {rate} years is : £ {total_amount}")

    else :
        print("You have not entered a valid input. Please try again.")
    

#Calulating the total amount of money if the user inputs bond 
if user_entry == "bond" :
    present_value = int(input("Please enter the present value of your house : "))
    rate          = int(input("Please enter the interest rate (in %) : "))
    time          = int(input("Please enter the number of months you plan to take to repay the bond : "))
    
    i = (rate / 100) / 12  #Calculating the monthly interest rate
    repayment = int((i * present_value) / (1 - ((1 + i) ** (-1 * time))))

    print(f"Your total monthly repayment will be £{repayment}")