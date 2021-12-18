import turtle
import math

r = int(input('nhap vao ban kinh hinh tron: '))

t= turtle.Turtle()
t.hideturtle()
t.pensize(1)
t.color('red')
t.circle(r)
turtle.done()

c= 2* math.pi*r
s= math.pi *r*r

print('chu vi hinh tron ban kinhs ={r} la {c}'.format(r=r,c=c))
print('dien tich hinh tron ban kinh = {r} la {s}'.format(r=r,s=s))