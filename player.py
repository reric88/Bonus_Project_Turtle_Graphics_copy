from turtle import Turtle

STARTING_POSITION = (0, -280)
# print(type(STARTING_POSITION))
MOVE_DISTANCE = (20)
FINISH_LINE_Y = (280)


class Player(Turtle):
    '''This is the Player class. You can add in move_forward, reset_turtle, crossed_finish_line'''
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('turtle')
        self.color('green')
        self.right(-90)
        self.goto(0, -280)
    
    def move_forward(self):
        new_y_coordinate = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y_coordinate)
    
    def reset_turtle_position(self):
        self.goto(STARTING_POSITION)

    def crossed_finish_line(self):
        if (self.ycor() > FINISH_LINE_Y):
            return True
        else:
            return False