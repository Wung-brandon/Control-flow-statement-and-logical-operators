
#conditional statements concepts
#BMI = weight/height*height

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))

BMI = round(weight/height**2)
if BMI < 18.5:
    print(f"Your BMI is {BMI} so You are Underweight")
elif BMI > 18.5 and BMI < 25:
    print(f"Your BMI is {BMI} so You are Normal weight")
elif BMI > 25 and BMI < 30:
    print(f"Your BMI is {BMI} so You are overweight")
elif BMI > 30 and BMI < 35:
    print(f"Your BMI is {BMI} so You are obese")
elif BMI > 35:
    print(f"Your BMI is {BMI} so You are clinically obese")
else:
    print("You are overbased")