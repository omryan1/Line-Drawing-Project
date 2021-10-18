#Initialize Turtle
import turtle
t = turtle.Turtle()
t.left(180)
t.speed(10)

#Functions
def drawBody():
    for i in range(180):
        t.forward(2)
        t.right(1)
    t.left(90)
    for i in range(90):
        t.forward(0.5)
        t.left(1)
    t.right(150)
    t.forward(20)
    t.right(70)
    for i in range(90):
        t.forward(0.55)
        t.right(0.6)
    t.left(180)
    
def drawLeaf():
    for i in range(60):
        t.forward(1.2)
        t.right(1.3)
    for i in range(40):
        t.forward(1.1)
        t.left(1.1)
    t.right(130)
    for i in range(65):
        t.forward(2.1)
        t.right(1.85)
    t.right(100)
    for i in range(45):
        t.forward(1.5)
        t.right(1.2)

def drawBody2():
    t.penup()
    t.setposition(57,222)
    t.pendown()
    t.right(30)
    for i in range(100):
        t.forward(2)
        t.right(1)

def drawSlice():
    t.penup()
    t.setposition(170,20)
    t.pendown()
    t.right(107)
    for i in range(155):
        t.forward(1.8)
        t.left(1)
    t.left(102)
    t.forward(202)
    t.right(180)
    t.forward(20)
    t.right(80)
    for i in range(136):
        t.forward(1.7)
        t.left(1.2)
    t.penup()
    t.setposition(93,-20)
    t.pendown()
    t.right(170)
    for i in range(132):
        t.forward(0.3)
        t.left(1.4)

def drawRays():
    t.penup()
    t.setposition(90,-15)
    t.pendown()
    t.left(100)
    t.forward(62)
    t.penup()
    t.setposition(84,-13)
    t.pendown()
    t.left(37)
    t.forward(57)
    t.penup()
    t.setposition(76,-14)
    t.pendown()
    t.left(30)
    t.forward(55)
    t.penup()
    t.setposition(71,-20)
    t.pendown()
    t.left(43)
    t.forward(59)
    t.penup()
    t.setposition(69,-30)
    t.pendown()
    t.left(27)
    t.forward(65)
    
def drawFace():
    t.penup()
    t.setposition(-5,160)
    t.pendown()
    t.dot(7)
    t.penup()
    t.setposition(15,163)
    t.pendown()
    t.dot(7)
    t.penup()
    t.setposition(-75,130)
    t.left(155)
    t.pendown()
    for i in range(83):
        t.forward(2.2)
        t.left(0.95)
    t.penup()
    t.setposition(75,185)
    t.right(95)
    t.pendown()
    for i in range(55):
        t.forward(0.5)
        t.left(0.5)

def drawPicture():
    drawBody()
    drawLeaf()
    drawBody2()
    drawSlice()
    drawRays()
    drawFace()

#Main
drawPicture()
