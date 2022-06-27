"""Calculate the BMI index"""

height = input("Enter your height in m : ")
weight = input("Enter your weight in kg : ")

bmi = str(int(int(weight)/(float(height)**2)))
print("your BMI is : "+bmi)