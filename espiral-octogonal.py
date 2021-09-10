# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:33:37 2019

@author: Usuario
"""

import turtle

wn=turtle.Screen().bgcolor("black")
al=turtle.Turtle()
al.color("blue")
al.hideturtle()

for i in range(200):
    al.forward(i)
    al.left(360/8)
    al.speed(50)

al.reset()