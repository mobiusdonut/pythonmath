from turtle import *
shape('turtle')
def square():
    for i in range(4):
        forward(100)
        right(90)
def squareloop():
    for i in range(60):
        square()
        right(5)
squareloop()
