from turtle import *
shape('turtle')
def square(sidelength):
    for i in range(4):
        forward(sidelength)
        right(90)
def squareloop():
    for i in range(60):
        square(1 + 5 * i)
        right(5)
squareloop()
