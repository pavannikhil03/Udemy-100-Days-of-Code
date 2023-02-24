from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time


screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while(game_is_on):
    screen.update()
    # time.sleep(0.1)
    ball.move()

    #detect collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or (ball.distance(l_paddle) < 50 and ball.xcor() < -330):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()




screen.exitonclick()