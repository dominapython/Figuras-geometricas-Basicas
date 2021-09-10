# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 12:38:57 2019

@author: Usuario
"""

import turtle
import random


wn=turtle.Screen().bgcolor("black")
colors=["blue","slateblue","orange","lightgreen","violet","palevioletred","mediumvioletred","cyan","plum","deeppink","fuchsia","springgreen","aquamarine"]
alex=turtle.Turtle()
alex.shape("turtle")
alex.color("cyan")
alex.penup()
alex.stamp()


for i in range(50):
    alex.forward(100)
    alex.stamp()
    alex.forward(-100)
    alex.right(36)
    alex.color(random.choice(colors))
    alex.speed(2)
    
alex.reset()