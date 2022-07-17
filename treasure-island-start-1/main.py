print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

side= input(" Think wisely, mind your step. You are at the cross-road now.\n Which direction would you like to go, left or right? L/R ")

if side=="L":
  swim_wait=input(" Fight or flight. COVID-19 infected zombies are after you. \n Time to decide, would you like to swim accross the water or wait? S/W ")
  if swim_wait=="S":
    door=input("Now it is time to make a life time decision. 3 doors 1 chance. \nAnswer is not your favorite color. \nWhich door would you like to open- yellow, red or blue? Y/R/B ")
    if door=="R":
      print("YOU WIN!! This girl is on fire! \n Deserved the song copy the link: https://www.youtube.com/watch?v=J91ti_MpdHA. ")
    else:
        print("What a shame! You blown up. Game is over.")
  else:
    print("Bloody! Eaten by the COVID(DED) ZOMBIES. Game over.")

else:
  print("Ooopps! You fall into a hole. Game over.")
#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload