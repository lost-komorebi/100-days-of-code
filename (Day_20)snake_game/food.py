#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

from turtle import Turtle
from random import choice


class Food(Turtle):

    def __init__(self):
        super(Food, self).__init__()
        self.penup()
        self.shape('circle')
        self.color('blue')
        self.refresh()

    def refresh(self):
        coordinates = []
        for i in range(280 + 1):
            if i % 20 == 0:
                coordinates.append(i)
        self.goto(choice(coordinates), choice(coordinates))
