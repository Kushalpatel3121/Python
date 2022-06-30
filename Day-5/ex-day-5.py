"""Password Generator"""

import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','@','$','%','&','*','(',')','_','-','+']

print("Welcome to password Generator!")
ps_letters = int(input("How many letters do you want in your password? "))
ps_numbers = int(input("How many numbers do you want in your password? "))
ps_symbols = int(input("How many symbols do you want in your password? "))

##Easy way to generate the easy password
password = ''
for n in range(0,ps_letters):
    temp = random.randint(0,len(letters)-1)
    password += letters[temp]
for n in range(0,ps_numbers):
    temp = random.choice(numbers)
    password += temp
for n in range(0,ps_symbols):
    temp = random.randint(0,len(symbols)-1)
    password += symbols[temp]
print(f"Your Password could be : {password}")

##Hard way to generate the Strong password
password = []
for n in range(0,ps_letters):
    temp = random.randint(0,len(letters)-1)
    password.append(letters[temp])
for n in range(0,ps_numbers):
    temp = random.choice(numbers)
    password += temp
for n in range(0,ps_symbols):
    temp = random.randint(0,len(symbols)-1)
    password.append(symbols[temp])
random.shuffle(password)
pswd = ''
for i in password:
    pswd += i
print(f"The Strong Password Generated is : {pswd}")
