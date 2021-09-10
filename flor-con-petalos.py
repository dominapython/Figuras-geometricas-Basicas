# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 11:11:46 2019

@author: Usuario
"""

import turtle
import random

wn=turtle.Screen().bgcolor("white")
colors=["aquamarine","slateblue","lightgreen","violet","palevioletred","mediumvioletred","cyan","plum","deeppink","fuchsia"]
flower=turtle.Turtle()
flower.color("cyan")
flower.hideturtle()
flower.shapesize(50)

for k in range(50):
    for i in range(2):
        flower.forward(100)
        flower.right(60)
        flower.forward(100)
        flower.right(120)


    flower.right(36)
    flower.color(random.choice(colors))
    
flower.reset()
flower.speed(20)
