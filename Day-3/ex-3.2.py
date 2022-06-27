"""Check the BMI"""

weight = float(input("Enter your weight in Kg : "))
height = float(input("Enter your height in m : "))

bmi = round(weight / height**2,3)

if bmi<=18.5:
    print(f"your bmi is {bmi} , you are underweight!")
elif bmi <= 25:
    print(f"your bmi is {bmi} , you have a normal weight")
elif bmi <= 30:
    print(f"your bmi is {bmi} , you are slighly overweight")
elif bmi <=35:
    print(f"your bmi is {bmi} , you are obese!")
else:
    print(f"your bmi is {bmi} , you are clinically obese!")