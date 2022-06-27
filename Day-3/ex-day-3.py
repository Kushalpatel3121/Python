"""Treasure Island Game"""

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to Treasure Island! Your Mission is to find the treasure")
choice1 = input("You're at crossroads , which way do you prefer to go? Type'right' or 'left' : ")
choice1.lower()
if choice1 == 'left':
    choice2 = input("You've reached a lake which you need to cross! , would you swim or would you wait for a boat? Type'wait' or 'swim'")
    choice2.lower()
    if choice2 == 'wait':
        choice3 = input("You're at a junction of 3 doors , which would you choose ? Red , Blue or Yellow? Type 'red' , 'blue' or 'yellow'")
        choice3.lower()
        if choice3 == 'yellow':
            print("You've found the treasure! You Won the Game")
        else:
            print("You Got disappeared into the black hole, Game Over!")
    else:
        print("You Drowned Yourself!, Game Over!")
else :
    print("You were eaten by a dinosaur! Game Over!")
