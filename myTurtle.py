import turtle

def drawTurtle():
    t = turtle.Turtle()
    t.color('red')
    t.forward(90)
    t.left(90)
    for c in ['green', 'blue', 'black']:
        t.color(c)
        t.forward(90)
        t.left(90)
    turtle.done()
