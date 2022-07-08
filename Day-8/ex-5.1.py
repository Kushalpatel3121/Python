"""Paint the Wall"""

import math

hgh = int(input("Enter the height of the wall : "))
wdth = int(input("Enter the width of the wall : "))
cvg = 5 #PER CAN

def calc_paint(height = hgh,width = wdth,coverage = cvg):
    area = height * width
    paint = area / coverage
    return (math.ceil(paint))
 
ans = calc_paint(hgh,wdth,cvg)
print(f"You will need {ans} cans of paint")


     