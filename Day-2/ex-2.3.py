"""Determine the number of days , weeks , months and years left"""

age = input("Enter your current age : ")
years = 90 - int(age)
months = years * 12
days = years * 365
weeks = years * 52

print(f"you have {days} days , {weeks} weeks , {months}  months remaining")