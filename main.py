from turtle import Screen,Turtle
from racket1 import Paddle1
from racket2 import Paddle2
from ball import Ball
import math
import time
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)
paddle1=Paddle1()
paddle2=Paddle2()
ball=Ball()
screen.listen()
screen.onkeypress(paddle1.up,"Up")
screen.onkeypress(paddle1.down,"Down")
screen.onkeypress(paddle2.up,"w")
screen.onkeypress(paddle2.down,"s")

game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    ball.move()
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()
    if abs(ball.ycor()-paddle1.ycor())<=30 and abs(ball.xcor()-paddle1.xcor())<=30 :
        ball.paddle_bounce()
    if abs(ball.ycor()-paddle2.ycor())<=30 and abs(ball.xcor()-paddle2.xcor())<=30 :
        ball.paddle_bounce()
    ball.passt()
screen.exitonclick()