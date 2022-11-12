#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'komorebi'

from turtle import Turtle
PACE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        start_position = 0
        for i in range(3):
            segment = self.create_segment(start_position, 0)
            start_position -= 20
            self.segments.append(segment)

    def create_segment(self, x, y):
        segment = Turtle('square')
        segment.color('white')
        segment.penup()
        segment.goto(x, y)
        return segment

    def extend(self):
        x = self.segments[-1].xcor()
        y = self.segments[-1].ycor()
        segment = self.create_segment(x, y)
        self.segments.append(segment)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            # move the last segment to the second last segment's position, then
            # move the last second last segment to the third last segment's
            # position, by doing this, we can move the snake consistently
            self.segments[i].goto(x, y)
        self.head.forward(PACE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
