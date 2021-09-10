# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 10:27:35 2019

@author: Usuario
"""

# draw a hexagon
import turtle

wn = turtle.Screen()
dijkstra = turtle.Turtle()

for i in range(6):
    dijkstra.forward(100)
    dijkstra.left(360/6)

dijkstra.reset()