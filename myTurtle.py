import turtle

def drawTurtle(wrapper):
    turtle.set_defaults(
        turtle_canvas_wrapper=wrapper
    )
    t = turtle.Turtle()

    t.width(5)
    t.color('red')
    t.forward(100)
    t.left(90)
    for c in [ 'green', 'blue', 'black']:
        t.color(c)
        t.forward(100)
        t.left(90)
    turtle.done()
