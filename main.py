import time
import turtle
from turtle import Turtle,Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.tracer(0)
my_screen.bgcolor("black")

my_turtle=Player()

my_title=Turtle()
my_title.color("white")
my_title.hideturtle()
my_title.penup()
my_title.goto(240,270)
my_title.write("FINISH LINE!",align="center" , font=("Courier", 10, "bold"))
my_title.goto(0,0)


my_cars = CarManager()
score_board=Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    my_screen.update()

    my_screen.listen()
    my_screen.onkey(my_turtle.up,"Up")
    my_screen.onkey(my_turtle.down,"Down")

   
    my_cars.new_cars()
    my_cars.move()

    if my_turtle.ycor()>275:
        my_turtle.level()
        my_cars.increase_level()
        score_board.increase_score()

    for cars in my_cars.all_cars:
        if cars.distance(my_turtle)<25:
            my_title.write("WOOPS,GAME OVER!!",align="center" , font=("Courier", 30, "bold"))
            
            name= turtle.textinput("Play Again Input","Do you want to play another game?")

            if name.lower()=="yes" or name.lower()=="y":
                my_cars.speed_reset()
                my_turtle.reset_player()
                score_board.reset_score()
                my_title.clear()
            
                continue
            else:
                score_board.game_over()
                my_title.clear()
                my_title.color("blue")
                my_title.write("Thanks for playing!!",align="center",font=("Courier", 25, "bold"))
                game_is_on=False

            

    

my_screen.exitonclick()