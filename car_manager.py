from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    
    def __init__(self):
        self.all_cars=[]
        self.speed=STARTING_MOVE_DISTANCE
        
    def new_cars(self):
        self.chance=random.randint(1,6)

        if self.chance==1:
            my_car=Turtle()
            my_car.penup()
            my_car.goto(250,random.randint(-230,230))
            my_car.shape("square")
            my_car.shapesize(1,2)
            my_car.setheading(180)
            my_car.color(random.choice(COLORS))
            self.all_cars.append(my_car)

    def increase_level(self):
        self.speed=self.speed+MOVE_INCREMENT


    def move(self):
        for cars in self.all_cars:
            cars.forward(self.speed)

    def speed_reset(self):
        self.speed=STARTING_MOVE_DISTANCE
    


