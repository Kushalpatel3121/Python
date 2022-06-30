"""Rock , Paper and Scissors Game"""
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''' 

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = int(input("Enter a choice : 0 for rock , 1 for paper , 2 for scissors : "))
symbols = [rock,paper,scissors]
computer_choice = random.choice(symbols)
if choice < 3:
    print(f"Your Choice : {symbols[choice]}")
    print(f"Computer's Choice : {computer_choice}")

if choice == 0:
    if computer_choice == rock:
        print("It's a Draw!")
    elif computer_choice == paper:
        print("Oops! , You Lost it!")
    else:
        print("Hurray! You won!")
elif choice == 1:
    if computer_choice == rock:
        print("Hurray! You won!")
    elif computer_choice == paper:
        print("It's a Draw!")
    else:
        print("Oops! , You Lost it!")
elif choice == 2:
    if computer_choice == rock:
        print("Oops! , You Lost it!")
    elif computer_choice == paper:
        print("Hurray! You won!")
    else:
        print("It's a Draw!")
else:
    print("Invalid Choice")