"""Basic Data Types , Number Operations"""

name = "kushal"
char = len(name)
# print("name has "+len(name)+" characters") #error
length = str(char)
print("name has "+length+" characters")

print(round(8 / 3))
print(round(8/3,3)) #round upto 3 decimal places
print(round(4.55666666,4))
print(8//3) #floor division

#f strings are the strings where we do not have to worry about type converions

score = 9.7
passed = True

print(f"your name is {name} , your score is {score} and your status is {passed}")