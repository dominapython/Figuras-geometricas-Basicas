# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 10:59:44 2019

@author: Usuario
"""

import turtle
import random


wn=turtle.Screen().bgcolor("black")
colors=["blue","slateblue","orange","lightgreen","violet","palevioletred","mediumvioletred","cyan","plum","deeppink","fuchsia","springgreen","aquamarine"]
alex=turtle.Turtle()
alex.color("cyan")
alex.penup()

for i in range(300):
    alex.forward(i)
    alex.right(185)
    alex.color(random.choice(colors))
    alex.speed(100)
    alex.stamp()
   
