"""Hangman Project"""

import random
word_list = ['cricket','football','beekeeper']
chosen = random.choice(word_list)

guess = input("Enter your choice : ")
guess.lower()

for i in range(0,len(chosen)):
    if guess == chosen[i]:
        print("Right")
    else:
        print("Wrong")

