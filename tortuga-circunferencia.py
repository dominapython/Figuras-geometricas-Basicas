# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 11:01:36 2019

@author: Usuario
"""

import turtle
import random


wn=turtle.Screen().bgcolor("black")
colors=["blue","slateblue","orange","lightgreen","violet","palevioletred","mediumvioletred","cyan","plum","deeppink","fuchsia","springgreen","aquamarine"]
alex=turtle.Turtle()
alex.shape("turtle")
alex.color("cyan")
alex.hideturtle()

for i in range(30):
    alex.right(185)
    alex.stamp()
    alex.forward(200)
    alex.right(70)
    alex.color(random.choice(colors))
    alex.speed(10)
    
alex.reset()
  