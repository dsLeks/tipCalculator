print("Welcome to the Tip Calculator!")
total_bill = float(input("What was the total bill? $"))
tip_percent = float(
    input("Would you like to give 15% tip, 20% tip, or 25% tip? "))
people = int(input("How many people to split the bill? "))
tip = tip_percent / 100 * total_bill + total_bill
split = tip / people
print(f"Each person should pay: $ {round(split,2)}")
