from turtle import Screen
from paddle import Paddle
from screen import GameScreen
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

game_screen = GameScreen()
scores = Scoreboard()
pong = Ball()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))


screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(pong.move_speed)
    pong.move()
    if pong.ycor() > 280 or pong.ycor() < -280:
        pong.bounce_y()
    if pong.distance(r_paddle) < 50 and pong.xcor() > 320 or pong.distance(l_paddle) < 50 and pong.xcor() < -320:
        pong.bounce_x()
    if pong.xcor() > 380:
        pong.reset_position()
        scores.l_point()
    if pong.xcor() < -380:
        pong.reset_position()
        scores.r_point()

screen.exitonclick()
