#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super(Ball, self).__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.x_pace = 10
        self.y_pace = 10

    def move(self):
        new_x = self.xcor() + self.x_pace
        new_y = self.ycor() + self.y_pace
        self.goto(new_x, new_y)

    def bounce_y(self):
        # each time change the direction
        self.y_pace *= -1

    def bounce_x(self, is_speed_up: int):
        # each time change the direction and speed up a little
        if is_speed_up == 1:
            self.x_pace *= -1.1
        else:
            self.x_pace *= -1

    def miss(self):
        self.goto(0, 0)
        self.bounce_x(0)
