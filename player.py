from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10



class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.color("white")
        self.penup()
        self.goto(STARTING_POSITION)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.backward(MOVE_DISTANCE)

    def level(self):
        self.goto(STARTING_POSITION)

    def reset_player(self):
        self.goto(STARTING_POSITION)
