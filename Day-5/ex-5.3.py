"""Calculate the sum all even numbers between 1 to 100"""
sum = 0
for n in range(2,101,2):
    sum += n

print(f"The Total sum is : {sum}")