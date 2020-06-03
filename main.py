import turtle
turtle.set_defaults(
    turtle_canvas_wrapper = document['turtle-div']
)
t = turtle.Turtle()

t.width(5)

for c in ['red', '#00ff00', '#fa0', 'rgb(0,0,200)']:
    t.color(c)
    t.forward(100)
    t.left(90)

# dot() and write() do not require the pen to be down
t.penup()
t.goto(-30, -100)
t.dot(40, 'rgba(255, 0, 0, 0.5')
t.goto(30, -100)
t.dot(40, 'rgba(0, 255, 0, 0.5')
t.goto(0, -70)
t.dot(40, 'rgba(0, 0, 255, 0.5')

t.goto(0, 125)
t.color('purple')
t.write("I love Brython!", font=("Arial", 20, "normal"))


turtle.done()