# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
"""lengthNames= int(len(names))
#last index is 1 less than the length of the items- since the positions start at 0
luckyStrike=int(random.randint(0,lengthNames-1))
person_to_pay= names[luckyStrike]
#print(f" {person_to_pay} is going to buy the meal today!")
print(person_to_pay + " is going to buy the meal today.") """

print(random.choice(names)+" is going to but the meal today.")


