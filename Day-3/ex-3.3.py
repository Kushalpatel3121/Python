"""Check whether a year is leap or not!"""

year = int(input("Enter a year : "))
if year % 100 == 0:
    if(year % 400 == 0):
        print("Leap Year!")
    else:
        print("not leap year!")
else:
    if(year % 4 == 0):
        print("Leap Year!")
    else:
        print("not Leap Year!")