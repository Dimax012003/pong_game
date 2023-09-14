from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.color("white")
        self.speed("fastest")
        self.goto(0,0)
        self.yspeed = 20
        self.xspeed = 10
    def move(self):

        self.setpos(self.xcor() + self.xspeed, self.ycor() - self.yspeed)
    def bounce(self):
        self.yspeed*=-1
    def paddle_bounce(self):
        self.xspeed*=-1
    def passt(self):
        if self.xcor()>390:
            self.setpos(0,0)
        elif self.xcor()<-390:
            self.setpos(0,0)
