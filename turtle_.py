import turtle
from random import randint


line = turtle.Turtle()
line.speed(0)
line.penup()
line.goto(-250,150)
line.pendown()

for i in range(21):
    line.write(i, align='center')
    line.right(90)
    line.forward(300)
    line.penup()
    line.backward(300)
    line.left(90)
    line.forward(25)
    line.pendown()
    
turtle_1 = turtle.Turtle()
turtle_2 = turtle.Turtle()
turtle_3 = turtle.Turtle()
turtle_4 = turtle.Turtle()
turtle_5 = turtle.Turtle()
turtle_6 = turtle.Turtle()
turtle_7 = turtle.Turtle()
turtle_8 = turtle.Turtle()
turtle_9 = turtle.Turtle()
turtle_10 = turtle.Turtle()

turtle_list=[turtle_1,turtle_2,turtle_3,turtle_4,turtle_5,turtle_6,turtle_7,turtle_8,turtle_9,turtle_10 ]

colors=['red','green','blue','yellow','grey','black','orange','pink','brown','purple']
for i in range(10):
    turtle_list[i].shape('turtle')
    turtle_list[i].color(colors[i],colors[i])
    turtle_list[i].penup()
    turtle_list[i].goto(-290,140-i*30)
    turtle_list[i].speed(0)

boolean=False
while not boolean:
    for k in turtle_list:
        k.forward(randint(20,50)/5)
        if k.xcor() >= 255:
            k.turtlesize(2)
            boolean = True
            break

turtle.done()