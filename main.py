import turtle
turtle.Screen().bgcolor("Hot pink")
turtle.Screen().setup(300,400)

pen =turtle.Turtle()
pen.color("violet")
pen.width(2)

size=0
while True:
    for i in range(4):
        pen.fd(size+1)
        pen.left(90)
        size=size-5
    size=size+1

turtle.done()