# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:28:40 2019

@author: Usuario
"""

# draw an octogon
import turtle

wn = turtle.Screen()
knuth = turtle.Turtle()

for i in range(8):
    knuth.forward(75)
    knuth.left(360/8)

knuth.reset()