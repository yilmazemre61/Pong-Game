from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
"""When we set the tracer to 0 if turns off the whole animation and we cannot see the paddle.
    To solve this problem we need to update the screen before we start doing something. We need to create a WHILE loop"""
screen.tracer(0)  # Turn OFF the animation

# Paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
# Ball
ball = Ball()
# Scoreboard
scoreboard = Scoreboard()

"""Set the movement"""
screen.listen()
# Right Paddle
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
# Left Paddle
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

"""Update for tracer"""
game_is_on = True

while game_is_on:
    if ball.ball_speed < 0:
        ball.ball_speed = 0.1
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # Detect collision with the wall and paddle
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    elif ball.xcor() > 325 and ball.distance(r_paddle) < 50:
        ball.bounce_x()
    elif ball.xcor() < -325 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    # If the right and left paddle misses
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.left_score()

    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.right_score()


screen.exitonclick()