import math
a=float(input("nhap vao a: "))
b=float(input("nhap vao b: "))
c=float(input("nhap vao c: "))

s= (a+b+c)/2

area = math.sqrt(s*(s-a)*(s-b)*(s-c))

print('Area of the triangle is: ',area)