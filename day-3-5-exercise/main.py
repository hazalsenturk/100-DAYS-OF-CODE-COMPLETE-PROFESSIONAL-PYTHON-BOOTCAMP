# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1=name1.lower()
name2=name2.lower()
name_combine=name1+" "+name2
#print(name_combine)
#print(name1)
#print(name2)
score=str(name_combine.count("t")+name_combine.count("r")+name_combine.count("u")+name_combine.count("e"))+str(name_combine.count("l")+name_combine.count("o")+name_combine.count("v")+name_combine.count("e"))
score=int(score)

if score<10 or score>90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score>40 and score<50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
