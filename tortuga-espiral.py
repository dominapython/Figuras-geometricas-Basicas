# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 11:46:37 2019

@author: Usuario
"""

import turtle
import random

wn=turtle.Screen().bgcolor("black")
colors=["blue","slateblue","orange","lightgreen","violet","palevioletred","mediumvioletred","cyan","plum","deeppink","fuchsia"]
flower=turtle.Turtle()
flower.color("cyan")
flower.shape("turtle")
flower.penup()

for i in range(200):
    flower.forward(i)
    flower.right(185)
    flower.stamp()
    flower.color(random.choice(colors))
    flower.speed(50)

flower.reset()