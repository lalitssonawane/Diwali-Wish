from tkinter.font import ITALIC
from tkinter.ttk import Style
import turtle
import colorsys
import random

#Create a turtle screen
screen=turtle.Screen() 

#Define height and width of screen
screen.setup(1200,600)

#Define Background color of screen
screen.bgcolor('black')

#Initialize a variable for turtle
t=turtle.Turtle()

# Define title of program
turtle.title("Happy Diwali")
t.speed(10)
t.hideturtle()
hue=0.0
size=random.randint(10,200)
def write(message,pos):
        x,y=pos
        # Define color of the text
        t.pencolor("orange")
        t.penup()
        t.goto(x,y)
        # Defining font style and size
        style=('Arial',100)
        t.write(message,font=style)

write('Happy Diwali',(-380,-50))
def draw_firecrackers(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
t.color("red")
angle=0
for i in range(20):

    t.fd(50)
    draw_firecrackers(300,180)
    angle+=18
    t.left(angle)
draw_firecrackers(450,180)
t.color("blue")
angle=0
for i in range(20):
    t.fd(50)
    angle+=18
    t.left(angle)
    draw_firecrackers(450,180)
draw_firecrackers(375,300)
t.color("green")
angle=0
for i in range(20):
    t.fd(50)
    angle+=18
    t.left(angle)
    draw_firecrackers(375,300)
draw_firecrackers(375,-300)
t.color("orange")
angle=0
for i in range(20):
    t.fd(50)
    angle+=18
    t.left(angle)
    draw_firecrackers(375,-300)
draw_firecrackers(150,-150)
t.color("violet")
angle=0
for i in range(20):
    t.fd(50)
    angle+=18
    t.left(angle)
    draw_firecrackers(150,-150)
draw_firecrackers(450,-150)
t.color("brown")
angle=0
for i in range(20):
    t.fd(50)
    angle+=18
    t.left(angle)
    draw_firecrackers(450,-150)
draw_firecrackers(-200,-300)
t.color("green")
angle=0
for i in range(20):
    t.fd(50)
    angle+=18
    t.left(angle)
    draw_firecrackers(-200,-300)
draw_firecrackers(125,0)
t.color("pink")
angle=0
draw_firecrackers(-100,-200)
for i in range(20):
    t.fd(50)
    angle+=18
    t.left(angle)
    draw_firecrackers(-100,-200) 
t.color("skyblue")
angle=0
draw_firecrackers(-500,-240)
for i in range(20):
    t.fd(50)
    angle+=18
    t.left(angle)
    draw_firecrackers(-500,-240)    
t.color("orange")
angle=0
draw_firecrackers(-350,-170)
for i in range(20):
    t.fd(50)
    angle+=18
    t.left(angle)
    draw_firecrackers(-350,-170)
t.color("pink")
angle=0
for i in range(20):
    t.fd(50)
    draw_firecrackers(-550,300)
    angle+=18
    t.left(angle)
draw_firecrackers(-450,180)


t.color("green")
angle=0
for i in range(20):
    t.fd(50)
    angle+=18
    t.left(angle)
    draw_firecrackers(-450,180)
draw_firecrackers(-375,300)
t.color("yellow")
angle=0
for i in range(20):
    t.fd(50)
    t.left(angle)
    angle+=18
    draw_firecrackers(-375,300)
draw_firecrackers(-375,-300)
screen.mainloop