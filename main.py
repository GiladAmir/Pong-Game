from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle
import time
from scoreboard import Scoreboard
SPEED = 0.1
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")
screen.tracer(0)
score = Scoreboard()


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
game_is_on = True

while game_is_on:
    time.sleep(SPEED)
    screen.update()
    ball.move()
    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 55 and ball.xcor() > 320 or ball.distance(l_paddle) < 55 and ball.xcor() < -320 :
        ball.bounce_x()
        SPEED *= 0.90
    # if ball.xcor() == 320:
    #     if ball.ycor() in range(int(r_paddle.ycor()) - 50, int(r_paddle.ycor()) + 50):
    #         ball.bounce_x()
    # elif ball.xcor() == -320:
    #     if ball.ycor() in range(int(l_paddle.ycor()) - 50, int(l_paddle.ycor()) + 50):
    #         ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.l_score_up()
        SPEED = 0.1
        ball.bounce_x()


    if ball.xcor() < -380:
        ball.reset_position()
        score.r_score_up()
        SPEED = 0.1
        ball.bounce_x()










screen.exitonclick()

