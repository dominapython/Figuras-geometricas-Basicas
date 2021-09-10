# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 12:48:07 2019

@author: Usuario
"""

import turtle

turtle.Screen().bgcolor("black")

turtle.Turtle()
turtle.color("blue")
turtle.hideturtle()


def hexagon():
  for _ in range(6):
      turtle.forward(100)
      turtle.left(360/3)

for i in range (6):
    hexagon()
    turtle.forward(100)
    turtle.right(60)

turtle.reset()
                 