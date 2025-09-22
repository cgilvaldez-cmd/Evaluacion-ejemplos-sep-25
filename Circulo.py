# -*- coding: utf-8 -*-
"""
Created on Mon Sep  8 16:01:57 2025

@author: Carlos Gil
"""
import turtle
import random


screen = turtle.Screen()


screen.setup(width=800, height=600)

t = turtle.Turtle()
t.speed(0)
t.pensize(3)
t.penup()

color= ["red", "blue", "green", "black"]



for i in range(50):
    x = -250 + i * 10
    y= i
    
    t.pencolor(random.choice(color))
    t.goto(x, y)
    t.pendown()
    t.circle(50)
    t.penup()
    

r= random.randint(10, 50)
t.circle(r)

turtle.done()

