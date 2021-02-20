from turtle import *
t1=Turtle()
t1.speed(-1000)
def draw(x):
    t1.right(10)
    for i in range(4):
        t1.forward(x)
        t1.right(90)
        t1.forward(x)
x=100
for j in range(10):
    for i in range(36):
        draw(x)
    x-=5
done()