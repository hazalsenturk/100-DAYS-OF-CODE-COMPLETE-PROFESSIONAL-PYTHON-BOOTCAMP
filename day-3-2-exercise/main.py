# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#also can write at a single line as BMI=round(weight/height**2)
BMI= weight/(height**2)
r_BMI=round(BMI)
if r_BMI<18.5:
  print(f"Your BMI is {r_BMI}, you are underweight.")
elif r_BMI<25:
  print(f"Your BMI is {r_BMI}, you have a normal weight.")
elif r_BMI<30:
  print(f"Your BMI is {r_BMI}, you are slightly overweight.")
elif r_BMI<35:
  print(f"Your BMI is {r_BMI}, you are obese.")
else:
  print(f"Your BMI is {r_BMI}, you are clinically obese.")

