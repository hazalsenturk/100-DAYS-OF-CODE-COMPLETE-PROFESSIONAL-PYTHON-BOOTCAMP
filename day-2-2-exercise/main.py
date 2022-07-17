# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Check the data type of the inputs.
print(type(height))
print(type(weight))
#Try to use the exponent operator in your code. Remember PEMDAS. 
#Remember to convert your result to a whole number (int)
BMI= (float(weight)/float(height)**2)
print(int(BMI))









