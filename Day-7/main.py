"""Hangman Project"""

import random
word_list = ['cricket','football','beekeeper']
chosen = random.choice(word_list)
display = []
for letter in chosen:
    display += '_'
lives = 6
end_of_game = False
while not end_of_game:
    guess = input("Enter your choice : ").lower()
    for i in range(0,len(chosen)):
        letter = chosen[i]
        if guess == letter:
            display[i] = letter
    if guess not in chosen:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose!")
    print(display)
    if "_" not in display:
        end_of_game = True
        print("You Win!")
