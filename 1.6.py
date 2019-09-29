from turtle import *
shape('turtle')
def star(sidelength):
    for i in range(5):
        forward(sidelength)
        right(144)
def starloop():
    for i in range(60):
        star(1 + 5 * i)
        right(5)
starloop()
