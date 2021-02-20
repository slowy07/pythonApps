from turtle import *

t1=Turtle()
t1.color('purple','pink')
t1.speed(40)
x=10
for i in range(10):
    t1.circle(x)
    x+=10
t1.right(180)
x=10
for i in range(10):
    t1.circle(x)
    x+=10
t1.right(90)
x=10
for i in range(10):
    t1.circle(x)
    x+=10
t1.right(-180)
x=10
for i in range(10):
    t1.circle(x)
    x+=10

done()