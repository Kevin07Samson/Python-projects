import time
import random
from turtle import Screen

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
scoreboard = Scoreboard()
screen = Screen()
player = Player()
cars = CarManager()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.onkey(player.move_up, "Up")
screen.listen()
level = 1
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if random.randint(1, 6) == 1:
        cars.create_car()

    cars.move_car()

    if cars.collision(player):
        game_is_on = False
        scoreboard.game_over()

    if player.is_at_finish_line():
        player.reset_position()
        scoreboard.increase_level()
        cars.level_up()
