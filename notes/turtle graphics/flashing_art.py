import turtle as t

t.speed(0)

'''
# octagon turns 45 degrees each time with 8 sides
for i in range(8):
    t.forward(100)
    t.right(45)

t.mainloop()


# circle within circles


for i in range(10):
    t.circle(radius)
    radius += offset



# circle within circles with penup and pendown
for i in range(10):
    t.circle(radius)
    radius += offset
    t.penup()
    x = t.xcor()
    y = t.ycor() - offset
    t.goto(x, y)
    t.pendown()
'''

radius = 25
offset = 10


# circle within circles with penup and pendown
for i in range(1000):
    t.circle(radius)
    radius += offset
    t.penup()
    x = t.xcor()
    y = t.ycor() - offset
    t.goto(x, y)
    t.pendown()
    for j in range(5): 
        t.right(65)
        for k in range(50):
            if k % 2 == 0:
                t.width(0)
                t.color("white")
            elif k % 3 == 0:
                t.width(1)
                t.color("purple")
            elif k % 5 == 0:
                t.width(2)
                t.color("orange")
            elif k % 7 == 0:
                t.width(3)
                t.color("green")
            else:
                t.width(4)
                t.color("pink")
            t.circle(radius*k)
            t.right(45)
            for l in range(6): 
                if l < 3:
                    t.color("pink")
                else:
                    t.color("lightblue")
                t.circle(radius*l)
                t.right(45)



    
    
t.mainloop()