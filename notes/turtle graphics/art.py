# turtle graphics is a Python library for creating graphics 
import turtle

'''
# show turtle window
turtle.showturtle()

# draw a line
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)

# keep window open
turtle.done()
'''

NUM_CIRCLES = 36  # number of circles to draw
DEGREES = 10  # angle to turn
COLOR = "light green"  # color of circles

turtle.bgcolor("black")

t = turtle.Turtle()
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()
t.speed(0)  # fastest speed
t1.speed(0) 
t2.speed(0)   
t3.speed(0)
t4.speed(0) 
t1.up()
t1.goto(300, 300)
t2.up()
t2.goto(-300, -300)
t3.up()
t3.goto(-300, 300)
t4.up()
t4.goto(300, -300)
t.width(2)  # width of pen
t1.width(4)
t2.width(6)
t3.width(8)
t4.width(10)
t.color(COLOR)  # color of pen
t1.color("light blue")
t2.color("pink")
t3.color("gold")
t4.color("cyan")
t1.down()
t2.down()
t3.down()
t4.down()

for count in range(NUM_CIRCLES):
    t.circle(100)
    t1.circle(100)
    t2.circle(100)
    t3.circle(100)
    t4.circle(100)
    t.left(DEGREES)
    t1.right(DEGREES)
    t2.left(DEGREES)
    t3.right(DEGREES)
    t4.left(DEGREES)
    
turtle.mainloop()  # keep window open
