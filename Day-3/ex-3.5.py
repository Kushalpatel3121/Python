"""Love Calculator"""

name1 = input("Enter your name : ")
name2 = input("Enter a name : ")

name1.lower()
name2.lower()

digit1 = name1.count('t') + name2.count('t') + name1.count('r') + name2.count('r') + name1.count('u') + name2.count('u') + name1.count('e') + name2.count('e')

digit2 = name1.count('l') + name2.count('l') + name1.count('o') + name2.count('o') + name1.count('v') + name2.count('v') + name1.count('e') + name2.count('e')

sum = int(str(digit1) + str(digit2))

if sum < 10 or sum > 90:
    print(f"your score is {sum}, you go together like colke and mentos")
elif sum >=40 and sum <= 50:
    print(f"Your score is {sum} , you are alright together")
else:
    print(f"Your score is {sum}")