from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.y_pace = 10
        self.x_pace = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_pace
        new_y = self.ycor() + self.y_pace
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_pace *= -1

    def bounce_x(self):
        self.x_pace *= -1
        self.move_speed *= 0.9

    def miss(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
