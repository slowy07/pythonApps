import turtle, math, random

number_of_leaves = 15


def leaf(scale, r, g, b):
    turtle.color(r, g, b)
    turtle.begin_fill()
    for i in range(360):
        length = (90 - abs(90 - float(i % 180))) / scale
        turtle.forward(length)
        turtle.right(1)
    turtle.end_fill()


def main():
    turtle.hideturtle()
    turtle.speed(0)
    turtle.colormode(255)
    for i in range(number_of_leaves):
        r = 255
        g = random.randint(0, 100)
        b = random.randint(0, 100)
        leaf(20, r, g, b)
        turtle.left(360 / number_of_leaves)
    turtle.getcanvas().postscript(file="flower.eps")


if __name__ == "__main__":
    main()
