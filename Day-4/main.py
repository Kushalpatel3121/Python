"""Randomization and Lists in Python"""

import random
import greetings  # we can import module in python like this

print(greetings.greet)
a = random.randint(3,90)
print(a)

b = random.random()
print(b)
print(b*5)      # to print the decimal numbers from 0 to 5


##Lists
#Lists can have data of mixed types
#In lists , the order of elements is important

names = ["Kushal" , "Rudra" , "Nitin" , "Harsha" , 1 ,2 ,3 ,4]
print(names[0])
print(names[5])
print(names[-1])  ## prints 4
print(names[-5])    ## prints Harsha
names[6] = 78
names.append("A family")
names.extend([4,5,6,7,8,9])
print(names)

fruits = ["apple","banana","mango"]
vegetables = ["spinach","corriander","onion","tomatoes"]

food = [fruits,vegetables]
print(food)