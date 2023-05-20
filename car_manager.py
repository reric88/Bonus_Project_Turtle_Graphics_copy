from turtle import Turtle
import random
import time
import math
from scoreboard import Scoreboard

COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
CAR_MOVE_DISTANCE = 1

def check_collision(car1, car2):
    car1_left = car1.xcor() - car1.shapesize()[1] * 10
    car1_right = car1.xcor() + car1.shapesize()[1] * 10
    car1_bottom = car1.ycor() - car1.shapesize()[0] * 10
    car1_top = car1.ycor() + car1.shapesize()[0] * 10

    car2_left = car2.xcor() - car2.shapesize()[1] * 10
    car2_right = car2.xcor() + car2.shapesize()[1] * 10
    car2_bottom = car2.ycor() - car2.shapesize()[0] * 10
    car2_top = car2.ycor() + car2.shapesize()[0] * 10

    if car1_left <= car2_right and car1_right >= car2_left and car1_bottom <= car2_top and car1_top >= car2_bottom:
        return True
    else:
        return False




class CarManager():
    def __init__(self):
        self.all_cars = []
        self.speed = CAR_MOVE_DISTANCE
        self.last_spawn_time = time.time()
        self.spawn_timer = 1

    def create_car(self):
        random_chance = random.randrange(1, 4)
        if len(self.all_cars) >= 20:
            return
        if random_chance == 1:
            current_time = time.time()
            time_elapsed = current_time - self.last_spawn_time
            if time_elapsed > self.spawn_timer:
                new_car = Turtle('square')
                new_car.penup()
                new_car.shapesize(stretch_wid=1, stretch_len=random.randint(2, 3))
                new_car.color(random.choice(COLORS)) 
                random_y_position = (random.randint(-6, 7) * 40)
                # random_y_position = 0
                overlapping = False
                car_speed = self.speed + random.randrange(1, 100) / 100
                for car in self.all_cars:
                    while car.distance(300, random_y_position) < 40:
                        random_y_position += 40
                        if random_y_position >= 280:
                            random_y_position = -240
                        overlapping = True
                        break

                if not overlapping:
                    new_car.goto(300, random_y_position)
                    new_car.speed = car_speed
                    self.all_cars.append(new_car)
                    self.last_spawn_time = current_time

                if self.speed > 20:
                    self.speed = 20

                if self.spawn_timer < 0.1:
                    self.spawn_timer = 0.1

                print(self.spawn_timer)
                print(self.speed)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(car.speed)
            if car.xcor() < -350:
                car.hideturtle()
                self.all_cars.remove(car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(car.speed)
            for other_car in self.all_cars:
                if car != other_car and check_collision(car, other_car):
                    move_up = car.ycor() + 40
                    move_down = car.ycor() - 40
                    direction = [move_up, move_down]
                    new_y = random.choice(direction)
                    car.sety(new_y)
                    break

            if car.xcor() < -350:
                car.hideturtle()
                self.all_cars.remove(car)

    def stop_cars(self):
        for car in self.all_cars:
            car.backward(0)

    def increase_speed(self):
        # self.speed += self.speed * random.randrange(1, 3)
        # self.speed += self.speed * random.randrange(1, 10) / 8
        self.speed += 1
        self.spawn_timer -= self.speed / 50

