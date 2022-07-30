from turtle import Turtle, Screen


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("black")
        self.shape("square")
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.penup()
        self.goto(position)
        self.speed("fastest")

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

