"""Output of a coin : Heads or Tails"""

import random

#set the seed to generate random numbers.
test_seed = int(input("Enter a seed number : "))
random.seed(test_seed)

num = random.randint(0,1)
if num == 1:
    print("Heads")
else:
    print("Tails")