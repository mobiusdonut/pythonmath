from turtle import *
shape('turtle')
def polygon(sides, sidelength):
    for i in range(sides):
        forward(sidelength)
        right(360.0 / sides)
polygon(17, 20)
