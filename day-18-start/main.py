import turtle as t
import random

# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("Da rkSeaGreen")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.speed(9)

tim = t.Turtle()
t.colormode(255)

# for i in range(4):
#     tim.forward(100)
#     tim.left(90)

# for i in range(15):
#     tim.pd()
#     tim.forward(10)
#     tim.pu()
#     tim.forward(10)

# turtle_color = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
# "SeaGreen"]

# sides = 3
# while sides in range(3, 11):
#     tim.color(random.choice(turtle_color))
#
#     for i in range(sides):
#         tim.forward(100)
#         tim.right(360 / sides)
#     sides += 1

# Random Walk

# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

tim.speed("fastest")

# Spirograph

for angle in range(0, 360, 5):
    tim.color(random_color())
    tim.setheading(angle)
    tim.circle(100)

screen = t.Screen()
screen.exitonclick()
