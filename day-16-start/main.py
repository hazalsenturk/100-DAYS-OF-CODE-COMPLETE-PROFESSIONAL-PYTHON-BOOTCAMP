# from turtle import Turtle, Screen
# # OR turtle.Turtle()
#
# # created new object from blueprint
# cingu = Turtle()
# print(cingu)
# # how to call methods associated with the object
# cingu.shape("turtle")
# cingu.shapesize(5, 5, 12)
# cingu.color("DarkSeaGreen3")
# cingu.forward(100)
# cingu.speed(1)
#
# my_screen = Screen()
# # how to tap into object attributes
# print(my_screen.canvheight)
# # canvas height also printed as an attribute
# my_screen.exitonclick()
# # allow program to exit screen on click

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmender"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
