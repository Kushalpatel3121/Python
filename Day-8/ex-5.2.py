"""Prime Number Checker"""

num = int(input("Enter a number"))

def prime_checker(num = num):
    is_prime = True
    for i in range(2,num-1):
       if num % i == 0: 
        is_prime = False

    if is_prime:
        print("It's a prime number")
    else:
        print("It's not a prime number")    

prime_checker(num)
