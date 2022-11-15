#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'


from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super(Paddle, self).__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=10)
        self.color('blue')
        self.penup()
        self.goto(200, -280)

    def move_left(self):
        if self.xcor() >= -380:
            self.backward(100)

    def move_right(self):
        if self.xcor() <= 380:
            self.forward(100)
