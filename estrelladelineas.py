# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 11:10:42 2019

@author: Usuario
"""


import turtle
import random


wn=turtle.Screen().bgcolor("black")
colors=["blue","slateblue","orange","lightgreen","violet","palevioletred","mediumvioletred","cyan","plum","deeppink","fuchsia","springgreen","aquamarine"]
linea=turtle.Turtle()
linea.hideturtle()
linea.color("cyan")
linea.hideturtle()


for i in range(50):
    linea.penup()
    linea.forward(50)
    linea.pendown()
    linea.backward(50)
    
    linea.right(36)
    
    linea.color(random.choice(colors))
    linea.speed(1)
    linea.penup()
    
    
linea.reset()