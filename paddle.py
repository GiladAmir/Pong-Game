from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,posotion):
        super().__init__()
        self.position = ()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(posotion)

    def create_paddle(self):
        pass


    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)




