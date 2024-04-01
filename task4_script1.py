from turtle import Turtle,Screen
def go_to(x,y):
    t.speed(10)
    t.hideturtle()
    t.penup()
    t.goto(x,y)
    t.speed(5)
    t.showturtle()
    t.pendown()
t = Turtle()
x = 180
screen = Screen()
screen.bgcolor("green")
screen.title("latargi")
t.pensize(5)
go_to(x,100)
t.right(90)
for i in range(3):#لا
    t.fd(100)
    t.rt(90)
go_to(x-150,50)
t.right(90)
for i in range(2):#ت
    t.fd(50)
    t.rt(90)
t.right(180)
for i in range(2):#ر
    t.fd(50)
    t.rt(90)
go_to(x-170,50)
t.dot(10)
go_to(x-190,50)
t.dot(10)
go_to(x-300,50)
t.right(90)
for i in range(3):
    t.fd(50)
    t.right(90)
t.right(180)
for i in range(3):
    t.fd(50)
    t.right(90)
go_to(-95,-25)
t.dot(10)
screen.mainloop()

