# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:14:05 2019

@author: Usuario
"""

import turtle


wn=turtle.Screen().bgcolor("black")
strella=turtle.Turtle()
strella.hideturtle()
strella.color("cyan")

for i in range(10):
    strella.forward(100)
    strella.left(216)
    
strella.reset()