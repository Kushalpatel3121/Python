"""Who's Paying the bill """

import random

test_seed = int(input("Enter a seed number : "))
random.seed(test_seed)

names = input("Enter the names , separated by a ',' and a space : ")
name = names.split(", ")

index = random.randint(0,len(name)-1)

print(f"{name[index]} is going to pay the bill!")

##Another way
payer = random.choice(name)
print(f"{payer} will pay the bill!")