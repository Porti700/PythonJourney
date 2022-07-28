# tip calculator
print("Welcome to the tip calculator")
total = float(input("What was the total bill?"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

per_tip = total * (tip/100)
final_bill = total+per_tip
people_split= round(final_bill/people, 2)

print(f"each person should pay: ${people_split} ")
