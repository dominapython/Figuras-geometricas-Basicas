# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 12:42:05 2019

@author: Usuario
"""
import turtle

turtle.Screen().bgcolor("black")
turtle.Turtle()
turtle.color("yellow")
turtle.hideturtle()


def hexagon():
  for _ in range(6):
      turtle.forward(100)
      turtle.left(360/6)

for i in range (6):
    hexagon()
    turtle.forward(100)
    turtle.right(60)
    
turtle.reset()
                 