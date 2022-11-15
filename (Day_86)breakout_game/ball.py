#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super(Ball, self).__init__()
        self.shape('circle')
        self.color('red')
        self.penup()
        self.x_pace = 5
        self.y_pace = 5
        self.width = 20
        self.height = 20

    def move(self):
        new_x = self.xcor() + self.x_pace
        new_y = self.ycor() + self.y_pace
        self.goto(new_x, new_y)

    def speed_up(self):
        self.x_pace *= 1.1
        self.y_pace *= 1.1

    def change_x(self):
        self.x_pace *= -1

    def change_y(self):
        self.y_pace *= -1

    def is_collision(self, other):
        """
        Axis-Aligned Bounding Box
        https://developer.mozilla.org/en-US/docs/Games/Techniques/2D_collision_detection
        """
        if self.xcor() < other.xcor() + other.width and\
                self.xcor() + self.width > other.xcor() and\
                self.ycor() < other.ycor() + other.height and\
                self.height + self.ycor() > other.ycor():
            return True
        return False

    def reset(self):
        self.x_pace = 5
        self.y_pace = 5
        self.goto(0, 0)
