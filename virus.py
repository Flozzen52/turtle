import turtle
turtle.speed(10)
ts=turtle.Screen()
ts.bgcolor("black")
t=turtle.Pen()
t.pencolor("white")
b=0
while b<200:
    t.right(b)
    t.forward(b*3)
    b+=1

