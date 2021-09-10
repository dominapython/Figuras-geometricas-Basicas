# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 15:03:36 2019

@author: Usuario
"""

import turtle


wn=turtle.Screen().bgcolor("black")
strella=turtle.Turtle()
strella.color('yellow')
strella.begin_fill()
strella.hideturtle()


for i in range(100):
    strella.forward(200)
    strella.left(170)
    

strella.end_fill()    
#strella.done()
strella.reset()









