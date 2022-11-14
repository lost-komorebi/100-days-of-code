from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super(CarManager, self).__init__()
        self.hideturtle()
        self.pace = STARTING_MOVE_DISTANCE
        self.car_fleet = []
        self.create_car()

    def create_car(self):
        chance = randint(1, 6)  # reduce the speed of car producing
        if chance == 6:
            car = Turtle('square')
            car.shape()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(choice(COLORS))
            car.penup()
            car.setheading(180)
            car.goto(300, randint(-250, 250))
            self.car_fleet.append(car)

    def move(self):
        for car in self.car_fleet:
            car.forward(self.pace)

    def speed_up(self):
        self.pace += MOVE_INCREMENT

    def reset(self):
        self.goto(300, randint(-250, 250))
