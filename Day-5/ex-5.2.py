"""Max Height"""

heights = input("Enter the Heights : ").split()
high = 0
for n in range(0,len(heights)):
    if high < int(heights[n]):
        high = int(heights[n])

print(f"The Max Height is : {high}")

##Another Way
print(f"The max height is : ",max(heights))