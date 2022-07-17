programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
  }

#Retrieving items from dictionary
print(programming_dictionary["Bug"])

#Adding new items to dictionary.
programming_dictionary["Loop"]="The action of doing something over and over again."
print(programming_dictionary)

empty_dictionary={}

#Wipe an existing dictionary, this can be used to wipe out a user info or to delete all tha player and score information when the game is over- to start a new game.
#programming_dictionary={}
#print(programming_dictionary)

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

#Loop through a dictionary- gives only the KEYs
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])
 

