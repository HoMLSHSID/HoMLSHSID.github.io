##Python Turtle
##Draw "HAPPY BIRTHDAY"
##Produced by Kaku, Kitetsu
##Version 0.0.1 Beta (I have no idea about the meaning of these numbers)
##Published on Feb 3, 2019

from turtle import*
import math
print()

def square(length):
    for i in range(4):
        t.fd(length)
        t.left(90)

def draw_square(x, y, length):
    t.up()
    t.goto(x, y)
    t.down()
    t.begin_fill()
    square(length)
    t.end_fill()

def rectangle(length, width):
    for i in range(2):
        t.fd(width)
        t.left(90)
        t.fd(length)
        t.left(90)

def draw_rectangle(length, width, x, y):
    t.hideturtle()
    t.up()
    t.goto(x, y)
    t.down()
    t.begin_fill()
    rectangle(length, width)
    t.end_fill()

def draw_pictures(x, y):
    t.up()
    t.goto(x, y)
    t.down()
    colors = ['red', 'yellow', 'green']
    for x in range(120):
        t.circle(x)
        t.color(colors[x % 3])
        t.left(60)

def move_to(x, y):
    t.up()
    t.goto(x, y)
    t.down()

def draw_arc(width, r):
    t.setheading(0)
    t.fd(width/3)
    t.setheading(180)
    t.circle(width/r, -180)
    t.setheading(180)
    t.fd(width/3)

def draw_h(x, y, height, width):
    move_to(x, y)
    t.setheading(270)
    t.fd(height)
    t.up()
    t.fd(-height/2)
    t.down()
    t.right(270)
    t.fd(width)
    t.up()
    t.left(90)
    t.fd(height/2)
    t.down()
    t.setheading(270)
    t.fd(height)

def draw_a(x, y, height, width):
    move_to(x, y)
    angle = math.degrees(math.atan((width/2) / height))
    t.setheading(270 - angle)
    t.fd(math.sqrt(math.pow(height, 2) + math.pow((width/2), 2)))
    t.up()
    move_to(x, y)
    t.down()
    t.setheading(270 + angle)
    t.fd(math.sqrt(math.pow(height, 2) + math.pow((width / 2), 2)))
    move_to(x - width/4, y - height/2)
    t.setheading(0)
    t.fd(width/2)

def draw_p(x, y, height, width):
    move_to(x, y)
    t.setheading(270)
    t.fd(height)
    move_to(x, y)
    draw_arc(width, 2)

def draw_y(x, y, height, width):
    move_to(x, y)
    t.setheading(300)
    t.fd(width)
    move_to(x + width, y)
    t.setheading(240)
    t.fd(width)
    t.setheading(270)
    t.fd(height - width*math.sqrt(3)/2)

def draw_b(x, y, height, width): #Debug required!
    move_to(x, y)
    t.setheading(270)
    t.fd(height)
    move_to(x, y)
    draw_arc(width, 2)
    draw_arc(width, 2)

def draw_i(x, y, height, width):
    move_to(x, y)
    t.setheading(0)
    t.fd(width)
    move_to(x + width / 2, y)
    t.setheading(270)
    t.fd(height)
    move_to(x, y - height)
    t.setheading(0)
    t.fd(width)

def draw_r(x, y, height, width): ##Debug required!
    move_to(x, y)
    t.setheading(270)
    t.fd(height)
    move_to(x, y)
    t.setheading(0)
    t.fd(width/4)
    t.setheading(180)
    t.circle(height/4, -180)
    t.fd(-width/4)
    t.setheading(315)
    t.fd((height/2) * math.sqrt(2))

def draw_t(x, y, height, width):
    move_to(x, y)
    t.setheading(0)
    t.fd(width)
    move_to(x + width / 2, y)
    t.setheading(270)
    t.fd(height)

def draw_d(x, y, height, width):
    move_to(x, y)
    t.setheading(270)
    t.fd(height)
    move_to(x, y)
    t.setheading(180)
    t.circle(height/2, -180)

def turtle_draw():
    draw_h(-300, 300, 200, 100)
    draw_a(-120, 300, 200, 100)
    draw_p(-50, 300, 200, 100)
    draw_p(60, 300, 200, 100)
    draw_y(170, 300, 200, 100)
    draw_b(-350, -50, 150, 75)
    draw_i(-275, -50, 150, 50)
    draw_r(-200, -50, 150, 100)
    draw_t(-130, -50, 150, 100)
    draw_h(-10, -50, 150, 75)
    draw_d(90, -50, 150, 100)
    draw_a(220, -50, 150, 100)
    draw_y(260, -50, 150, 75)

t = Turtle()
t.speed(0)
t.screen.bgcolor('black')
t.color('white')
t.pensize(3)
turtle_draw()
t.pensize(2)
t.screen.tracer(500, 500)
draw_pictures(0,0)

t.screen.exitonclick()
