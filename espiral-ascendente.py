# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 10:59:43 2019

@author: Usuario
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 11:11:46 2019

@author: Usuario
"""

import turtle
import random

wn=turtle.Screen().bgcolor("black")
colors=["blue","slateblue","orange","lightgreen","violet","palevioletred","mediumvioletred","cyan","plum","deeppink","fuchsia","springgreen","aquamarine"]
flower=turtle.Turtle()
flower.color("cyan")
flower.hideturtle()

for i in range(300):
    flower.forward(i)
    flower.right(185)
    flower.color(random.choice(colors))
    flower.speed(30)
    
flower.reset()

    
