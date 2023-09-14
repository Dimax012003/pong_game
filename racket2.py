from turtle import Turtle

class Paddle2(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.color("white")
        self.speed("fastest")
        self.goto(-350,0)
    def up(self):
        if self.ycor()<=280:
            self.setheading(0)
            self.goto(self.xcor(),self.ycor()+20)
    def down(self):
        if self.ycor()>=-280:
            self.setheading(180)
            self.goto(self.xcor(), self.ycor() -20)