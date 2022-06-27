"""Day-2 Final Project"""
"""Create the tip calculator"""

print("Welcome to the tip calculator!")
amount = input("Enter the total amount of bill : ")
percent = input("What percentage of tip would you like to give? ")
people = input("How many people to split the bill between ? ")

total = float(amount) + ((int(percent)/100)*float(amount))
amt_pp = round(total / int(people),2)

print(f"Each person should pay: ${amt_pp}")
