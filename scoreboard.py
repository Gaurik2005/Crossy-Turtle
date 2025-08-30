from turtle import Turtle

class Scoreboard():
    def __init__(self):
        self.score=0
        with open("high_score.txt","r") as file:
            self.high_score=int(file.read())

       
        self.my_score=Turtle()
        self.my_score.penup()
        self.my_score.color("white")
        self.my_score.goto(-190,270)
        self.my_score.hideturtle()
        self.my_score.write(f"Score : {self.score}  High Score : {self.high_score}",align="center" , font=("Courier", 10, "bold"))

    def increase_score(self):
        self.score+=1
        self.my_score.clear()
        self.my_score.write(f"Score : {self.score}  High Score : {self.high_score}",align="center" , font=("Courier", 10, "bold"))

    def reset_score(self):
        if self.score>self.high_score:
            self.high_score=self.score
        with open("high_score.txt","w") as file:
            file.write(f"{self.high_score}")

        self.score=0
        self.my_score.clear()
        self.my_score.write(f"Score : {self.score}  High Score : {self.high_score}",align="center" , font=("Courier", 10, "bold"))

    def game_over(self):
        if self.score>self.high_score:
            self.high_score=self.score
        with open("high_score.txt","w") as file:
            file.write(f"{self.high_score}")
