import turtle


def square(coast):
    for i in range(4):
        t.forward(coast)
        t.left(90)

def squares(starting_size, nb):
    for i in range(1, nb):
        square(i * starting_size)


t = turtle.Turtle()

squares(40, 10)

turtle.done()