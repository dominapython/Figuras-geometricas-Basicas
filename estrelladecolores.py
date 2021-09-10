# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:38:40 2019

@author: Usuario
"""

import turtle
import random


wn=turtle.Screen().bgcolor("black")
strella=turtle.Turtle()
colors=["blue","slateblue","orange","lightgreen","violet","palevioletred","mediumvioletred","cyan","plum","deeppink","fuchsia","springgreen","aquamarine"]
strella.hideturtle()
strella.color("cyan")


for i in range(300):
    strella.forward(i)
    strella.left(225)
    strella.speed(30)
    strella.color(random.choice(colors))
    
strella.reset()