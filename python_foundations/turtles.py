#! /usr/bin/env python

import turtle
import time


def draw_art():


    window = turtle.Screen()
    window.bgcolor("green")

    brad = turtle.Turtle()     # initiates an instance (object) of class Turtle()
    brad.shape("turtle")       # methods for class Turtle()
    brad.color("yellow")
    brad.speed(10)

    for i in range(36):
      draw_triangle(brad)
      brad.right(10)

    brad.right(90)
    brad.forward(250)


    window.exitonclick()


def draw_square(tname):

    for i in range(4):
        tname.forward(100)
        tname.right(90)


def draw_circle(tname):

    tname.circle(100)


def draw_triangle(tname):


    tname.forward(100)
    tname.left(120)
    tname.forward(100)
    tname.left(120)
    tname.forward(100)




draw_art()







