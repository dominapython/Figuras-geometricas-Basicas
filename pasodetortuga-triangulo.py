# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:54:29 2019

@author: Usuario
"""

import turtle

wn=turtle.Screen().bgcolor("black")
t=turtle.Turtle()
L=turtle.Turtle()
t.color("blue")
t.shape("turtle")
t.penup()
L.hideturtle()
L.color("red")

for i in range(3):
    L.forward(200)
    L.speed(2)
    L.right(360/3)
    t.forward(200)
    t.speed(2)
    t.right(360/3)
    t.stamp()

L.reset()
t.reset()