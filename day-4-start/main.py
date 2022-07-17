import random

#randint(a,b) will give random integer between [2-100] 
random_number= random.randint(2,100)
print(random_number)

#random() will give float number between [0,1), random() takes no arguement inside
rand_float= random.random()
print(rand_float)
#to create random floats between [0-5) with random() multiply it by 5
rand_float= random.random()*5
print(rand_float)