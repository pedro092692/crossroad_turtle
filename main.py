from turtle import Screen
from player import Player
from car_manager import Car
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("CROSS ROAD GAME")
screen.colormode(255)
screen.tracer(0)

player = Player()
car = Car(5)
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(key="Up", fun=player.move)

game_is_on = True

while game_is_on:
    time.sleep(car.cars_speed)
    screen.update()
    car.move_car()
    car.reset_car_position()

    # Detect collision with cars
    if car.collision_with_turtle(player):
        game_is_on = False
        scoreboard.game_over()

    # Detect when turtle hit the top
    if player.is_finish_line():
        car.create_cars(number_of_cars=1)
        car.increase_cars_speed()
        scoreboard.score_leve()




screen.exitonclick()

