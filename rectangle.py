import turtle
import math


w=int(input('enter width: '))
h=int(input('enter height: '))

t= turtle.Turtle()

t.hideturtle()
t.pensize(1)
t.color('red')
t.fillcolor('blue')
t.begin_fill()
t.forward(w)
t.right(90)
t.forward(h)
t.right(90)
t.forward(w)
t.right(90)
t.forward(h)
t.end_fill
turtle.done()

c= 2*(w+h)
s=w*h

print('chu vi hinh chu nhat: ',c)
print('dien tich hinh chu nhat: ',s)