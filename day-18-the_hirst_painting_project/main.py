# import colorgram

import turtle as t
import random

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 50)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(144, 76, 49), (188, 164, 120), (166, 153, 35), (14, 45, 83), (45, 110, 137), (142, 185, 175), (146, 55, 82), (59, 120, 100), (141, 169, 177), (86, 35, 29), (63, 152, 169), (219, 210, 94), (112, 37, 30), (101, 145, 111), (166, 98, 129), (94, 121, 170), (169, 144, 162), (178, 103, 83), (206, 183, 195), (50, 52, 90), (71, 38, 55), (93, 44, 63), (172, 201, 193), (172, 201, 204), (14, 101, 81), (4, 98, 119), (213, 180, 173), (180, 191, 207), (43, 45, 44)]

painter = t.Turtle()
t.colormode(255)

# 10 * 10 posts, dots_size = 20, spaced around=50


def draw_dot():
    painter.dot(20, random.choice(color_list))

painter.speed('normal')


for y_cord in range(-200, 300, 50):
    painter.penup()
    painter.setposition(-200, y_cord)

    for n in range(10):
        painter.pendown()
        draw_dot()
        painter.penup()
        painter.forward(50)
        n += 1




screen = t.Screen()
screen.screensize(500, 500)
screen.exitonclick()
