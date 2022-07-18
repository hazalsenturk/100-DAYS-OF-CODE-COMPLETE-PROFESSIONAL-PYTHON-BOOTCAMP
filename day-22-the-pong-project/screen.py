from turtle import Turtle

DASH_NUMBER = 50


class GameScreen(Turtle):

    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.pensize(10)
        self.draw_boundary()

    def draw_boundary(self):
        self.penup()
        self.goto(0, 400)
        self.setheading(270)
        for number in range(50):
            self.hideturtle()
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(20)
