from turtle import *
shape('turtle')
def triangle(sidelength):
    for i in range(3):
        forward(sidelength)
        right(120)
triangle(100)
