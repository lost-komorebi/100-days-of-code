#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

from turtle import Turtle
from random import choice
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class BrickManager(Turtle):

    def __init__(self):
        super(BrickManager, self).__init__()
        self.bricks = []
        self.bricks_number = 0
        self.create_brick()

    def create_brick(self):
        y = 250
        for i in range(6):
            y -= 25
            x = -460
            for _ in range(1000 // 65):
                brick = Turtle('square')
                brick.shapesize(stretch_wid=1, stretch_len=3)

                brick.color(choice(COLORS))
                brick.penup()
                brick.width = 60
                brick.height = 20
                brick.goto(x, y)
                x += 65
                self.bricks.append(brick)
                self.bricks_number += 1
