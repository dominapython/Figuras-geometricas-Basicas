# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 11:02:50 2019

@author: Usuario
"""

import turtle
import random

wn=turtle.Screen().bgcolor("black")
tanenbaum = turtle.Turtle()
colors=["blue","slateblue","orange","lightgreen","violet","palevioletred","mediumvioletred","cyan","plum","deeppink","fuchsia","springgreen","aquamarine"]
tanenbaum.hideturtle()
tanenbaum.speed(5)
tanenbaum.color("cyan")

for i in range(350):
    tanenbaum.forward(i)
    tanenbaum.right(98)
    tanenbaum.color(random.choice(colors))