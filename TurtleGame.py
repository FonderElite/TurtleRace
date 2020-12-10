import turtle
from turtle import *
from random import randint

#screen
screen = turtle.Screen()
screen.title("Turtle Race v1")
screen.bgcolor("light sky blue")
turtle.speed()
turtle.penup()
turtle.penup()
turtle.setpos(-200,180)
turtle.write("Turtle Race Game v1.0",font=("Courier New",30,"bold"))
turtle.pendown()
turtle.color('black')
#turtle
speed(10)
penup()
goto(-140,120)
for steps in range(24):
    write(steps,align="center")
    right(90)
    forward(10)
    pendown()
    forward(160)
    penup()
    backward(160)
    left(90)
    forward(20)

#turtle droid
droid = Turtle()
droid.color('green')
droid.shape('turtle')
droid.penup()
droid.goto(-160,100)
droid.pendown()

#turtle abalesluke
abalesluke = Turtle()
abalesluke.color('red')
abalesluke.shape('turtle')
abalesluke.goto(-200,60)
abalesluke.pendown()

#turtle warenjr

warenjr = Turtle()
warenjr.color("blue")
warenjr.shape('turtle')
warenjr.goto(-200,40)
warenjr.pendown()

#turtle dldygnl
htbpro = Turtle()
htbpro.color('yellow')
htbpro.shape('turtle')
htbpro.goto(-200,10)
htbpro.pendown()

if htbpro.color() == 'yellow':
    htbpro.goto(100,20)
#RACETIME!!!

for turn in range(100):
    droid.forward(randint(1,10))
    abalesluke.forward(randint(1,10))
    warenjr.forward(randint(1,10))
    htbpro.forward(randint(1,10))
