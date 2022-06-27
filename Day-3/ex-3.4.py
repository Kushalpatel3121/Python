"""Pizza Deliveries"""

size = input("Enter the size of the pizza : S , M or L? ")
pepperoni = input("Do you want pepperoni? Y or N ? ")
cheese = input("Do you want extra cheese? Y or N? ")
bill = 0
if size == 'S':
    bill = 15
    if pepperoni == 'Y':
        bill += 2
elif size == 'M':
    bill = 20
    if pepperoni == 'Y':
        bill += 3
elif size == 'L':
    bill = 25
    if pepperoni == 'Y':
        bill += 3
if cheese == 'Y':
    bill += 1
print(f"You Bill is ${bill}")