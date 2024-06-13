from turtle import *
tracer(0)
screensize(10000,10000)
cell = 30
left(90)

for i in range(2):
    forward(12*cell)
    right(90)
    forward(12*cell)
    right(90)

up()
forward(2*cell)
right(90)
forward(3*cell)
left(90)
down()

for z in range(2):
    forward(14*cell)
    right(90)
    forward(12*cell)
    right(90)
up()
for x in range(-20,40):
    for y in range(-20,40):
        goto(x*cell,y*cell)
        if x == 0 or y == 0:
            dot(5,"red")
        else:
            dot(3)

done()