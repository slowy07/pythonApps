import turtle

tData = turtle.Turtle()
tData.left(90)
tData.speed(200)

def getRet(i):
    if i < 10:
        return
    else:
        tData.forward(i)
        tData.left(30)
        getRet(3 * i / 4)
        tData.right(60)
        getRet(3 * i / 4)
        tData.left(30)
        tData.backward(i)

getRet(100)
turtle.done()
