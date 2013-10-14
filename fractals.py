import turtle
import math
from ColorReference import ColorReference

def sherp(depth, distance, colorRef):
    if depth > -1:
        turtle.fillcolor(colorRef.getColor(depth))
        turtle.begin_fill()
        for x in range(3): #just for drawing
            turtle.fd(distance)
            turtle.lt(120)
        turtle.end_fill()
        
        for x in range(3):
            turtle.fd(distance) #continue the sherpinski
            turtle.lt(120) #real sherpinski
            if depth == 0:
                turtle.begin_fill()
            sherp(depth-1, distance/2, colorRef)
            #turtle.lt(120) #messed up sherpinski
        turtle.end_fill()

def kochLine(depth, distance):
    if depth == 0:
        turtle.fd(distance)
    elif depth > 0:
        kochLine(depth-1, distance/3)
        turtle.rt(60)
        kochLine(depth-1, distance/3)
        turtle.lt(120)
        kochLine(depth-1, distance/3)
        turtle.rt(60)
        kochLine(depth-1, distance/3)

def koch(depth, distance):
    for x in range(3):
        kochLine(depth, distance)
        turtle.lt(120)



distance = 400.0
depth = 5

turtle.speed(0) #0 = fastest
turtle.ht()     #hideturtle
turtle.penup()
turtle.setx(-distance/2)
turtle.sety(-distance * math.sqrt(3) / 4)   #1/2 way up triangle
turtle.pendown()
turtle.colormode(255)

#koch(depth, distance)

colorRef = ColorReference(depth)
sherp(depth, distance, colorRef)
