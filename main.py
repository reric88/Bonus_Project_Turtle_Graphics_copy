import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import threading
from playsound import playsound
import sounddevice as sd
# from pydub import AudioSegment
# from pydub.playback import play
# You can import sound and music as well

splat = 'Sound/cartoon-splat-6086.mp3'
honk = 'Sound/car-horn-beep-beep-two-beeps-honk-honk-6188.mp3'
jump = 'Sound/boing-101318.mp3'
gameover = 'Sound/short-applause-96213.mp3'
level_up = 'Sound/the-notification-email-143029.mp3'
power_up = 'Sound/coin_c_02-102844.mp3'

def play_sound(sound):
    threading.Thread(target=playsound, args=(sound,)).start()
# def play_sound(path):
#     sound = AudioSegment.from_file(path)
#     play(sound)

def check_collision(car, player):
    car_left = car.xcor() - car.shapesize()[1] * 10
    car_right = car.xcor() + car.shapesize()[1] * 10
    car_bottom = car.ycor() - car.shapesize()[0] * 10
    car_top = car.ycor() + car.shapesize()[0] * 10

    player_left = player.xcor() - player.shapesize()[1]
    player_right = player.xcor() + player.shapesize()[1]
    player_bottom = player.ycor() - player.shapesize()[0]
    player_top = player.ycor() + player.shapesize()[0]


    # if car_left < player_right + 50 and car.ycor() == player.ycor():
    #     play_sound('Sound\car-horn-beep-beep-two-beeps-honk-honk-6188.mp3')
    # elif car_left < player_right and car_right >= player_left and car_bottom <= player_top and car_top >= player_bottom:
    if car_left < player_right and car_right >= player_left and car_bottom <= player_top and car_top >= player_bottom:
        # play_sound(splat)
        playsound(splat)
        return True
    else:
        return False




view_screen = Screen()
view_screen.setup(width=600, height=600)
view_screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

view_screen.listen()
view_screen.onkey(player.move_forward, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    view_screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    if player.crossed_finish_line():
        play_sound(level_up)
        player.reset_turtle_position()
        scoreboard.increase_level()
        car_manager.increase_speed()

    for car in car_manager.all_cars:
        if check_collision(car, player):
            game_is_on = False
            scoreboard.scoreboard_game_over()
            play_sound(gameover)

view_screen.exitonclick()