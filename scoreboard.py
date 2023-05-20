from turtle import Turtle

FONT = ('Courier', 24, 'normal')

returned_level = None

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        print('Creating Scoreboard')
        self.level = 1
        self.speed = 1
        self.color('black')
        self.penup()
        self.goto(-250, 250)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'Level: {self.level}', move=False, align='left', font=FONT)

    def scoreboard_game_over(self):
        self.goto(0, 0)
        self.write(f'Game Over, you made it to level {self.level}.', move=False, align='center', font=FONT)

    def increase_level(self):
        self.level += 1
        returned_level = self.level
        self.clear()
        self.update_scoreboard()
        return returned_level
    
    def increase_speed(self):
        self.speed = self.speed + (self.speed / 90)

    def stage_level(self):
        self.level += 1
        level = self.level
        return level
    
    level_var = returned_level