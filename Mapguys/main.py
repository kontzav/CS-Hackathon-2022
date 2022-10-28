import turtle


def grid():
    sc = turtle.Screen()
    trtl = turtle.Turtle()
    turtle.setworldcoordinates(-250, -250, 500, 500)

    # method to draw y-axis lines
    def drawy(val):
        # line
        trtl.forward(360)

        # set position
        trtl.up()
        trtl.setpos(val, 360)
        trtl.down()

        # another line
        trtl.backward(360)

        # set position again
        trtl.up()
        trtl.setpos(val + 10, 0)
        trtl.down()

    # method to draw y-axis lines
    def drawx(val):

        # line
        trtl.forward(360)

        # set position
        trtl.up()
        trtl.setpos(360, val)
        trtl.down()

        # another line
        trtl.backward(360)

        # set position again
        trtl.up()
        trtl.setpos(0, val + 10)
        trtl.down()

    # method to label the graph grid
    def lab():

        # set position
        trtl.penup()
        trtl.setpos(180, 180)
        trtl.pendown()

        # write 0
        trtl.write(0, font=("Verdana", 12, "bold"))

        # set position again
        trtl.penup()
        trtl.setpos(-20, 180)
        trtl.pendown()

        # write x
        trtl.write("x", font=("Verdana", 12, "bold"))

        # set position again
        trtl.penup()
        trtl.setpos(180, -20)
        trtl.pendown()

        # write y
        trtl.write("y", font=("Verdana", 12, "bold"))

    # Main Section
    # set screen
    sc.setup(600, 600)

    # set turtle features
    trtl.speed(180)
    trtl.left(90)
    trtl.color('lightgreen')

    # y lines
    for i in range(36):
        drawy(10 * (i + 1))

    # set position for x lines
    trtl.right(90)
    trtl.up()
    trtl.setpos(0, 0)
    trtl.down()

    # x lines
    for i in range(36):
        drawx(10 * (i + 1))

    # axis
    trtl.color('green')

    # set position for x axis
    trtl.up()
    trtl.setpos(0, 180)
    trtl.down()

    # x-axis
    trtl.forward(360)

    # set position for y axis
    trtl.left(90)
    trtl.up()
    trtl.setpos(180, 0)
    trtl.down()

    # y-axis
    trtl.forward(360)

    # labeling
    lab()

    # hide the turtle
    trtl.hideturtle()
    turtle.done()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    grid()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
