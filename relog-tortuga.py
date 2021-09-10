# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 15:22:55 2019

@author: Usuario
"""


import turtle


wn=turtle.Screen().bgcolor("black")
strella=turtle.Turtle()
strella.shape("turtle")
strella.color("cyan")
strella.stamp()
linea=turtle.Turtle()
linea.hideturtle()
linea.color("cyan")


for i in range(12):
    strella.penup()
    strella.forward(100)
    strella.stamp()
    
    strella.penup()
    strella.forward(-15)
    strella.pendown()
    strella.forward(-5)
    strella.penup()
    
    strella.forward(-80)
    strella.left(210)
    
    
strella.reset()
linea.reset()
      
