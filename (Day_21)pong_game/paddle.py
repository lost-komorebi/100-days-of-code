#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'


from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, coordinate: tuple):
        super(Paddle, self).__init__()
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.goto(coordinate)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
