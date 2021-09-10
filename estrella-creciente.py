# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:32:49 2019

@author: Usuario
"""

import turtle


wn=turtle.Screen().bgcolor("black")
strella=turtle.Turtle()
strella.hideturtle()
strella.color("cyan")

for i in range(100):
    strella.forward(i)
    strella.left(216)
    
strella.reset()
    