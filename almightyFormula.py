from math import *

a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
D=(pow(b,2)-4*a*c)
if (D<0):
    print("It has a complex root")
else:
    x1=(-b+sqrt(D))/2*a
    x2=(-b-sqrt(D))/2*a
    print("x= ", x1, "or ", x2)

