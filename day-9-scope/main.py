################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope

def drink_potion():
  potion_strength = 2 
  print(potion_strength)

drink_potion()
print(potion_strength) # will give error-since it is on local scope- defined in function only

# Global Scope

player_health = 10

def drink_potion():
  potion_strength = 2 
  print(player_health) #will be printed since it is on global scope- its not in another function, it is available within and outside of the functions 

drink_potion()
 
#There is no block scope in Pyhton

game_level = 3

def  create_enemy():
  enemies={"Skeleton","Zombies","Alien"}
  if game_level < 5:
    new_enemy = enemies[0]
  print(new_enemy) # this will be printed

#print(new_enemy) this will give error

#exlpanation: if not embedded in a function will print,  but if I embed the code in function create_enemy() then it will give idenfitication error so it needs to be printed in the function- within the function there is a local scope, if-while loops dont create a local function

#IF CREATE A VARIABLE WITHIN A FUNCTION_ IT WILL BE AVAILABLE ONLY IN FUNCTION

# Modifying Global Scope Variables 

enemies = 1

def increase_enemies():
  print(f"enemies inside function: {enemies}")
  return enemies+1

increase_enemies()
print(f"enemies outside function: {enemies}")

#Global Scope: useful to create constants- for the values you never want to change
pi = 3.14156 

#in Python naming convention for the constants. e.g.

PI= 3.145
URL="https://www.google.com"

def calc():
  URL
  PI #this upper case convention reminds 



