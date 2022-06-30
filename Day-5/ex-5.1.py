"""Average Student's Height"""

heights = input("Enter the Heights of the students separated by a ',' : ").split(",")
count =0
total = 0
for n in range(0,len(heights)):
    total += int(heights[n])
    count += 1
avg = total / count
print(f"The Average height of students is : {avg}")


##Another Way
ans = sum(heights)/len(heights)
print(f"Average = {ans}")