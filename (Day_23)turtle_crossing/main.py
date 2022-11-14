import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()


screen.listen()
screen.onkey(player.move, 'Up')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    car_manager.create_car()
    car_manager.move()

    # detect turtle with car
    for car in car_manager.car_fleet:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detect turtle with up wall
    if player.ycor() >= 290:
        scoreboard.add_score()
        player.reset()
        car_manager.speed_up()

screen.exitonclick()
