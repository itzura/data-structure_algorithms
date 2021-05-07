import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()
myTurtle.penup()
myTurtle.goto(-myWin.window_width()+5,myWin.window_height()*2/3 - 20)
myTurtle.pendown()


def drawSpiral(myTurtle,lineLen):
    if lineLen>0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle, lineLen-5)



drawSpiral(myTurtle,820)
myWin.exitonclick()