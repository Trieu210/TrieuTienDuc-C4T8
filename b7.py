import math 

a = float(input("a ="))
b = float(input('b ='))
c = float(input('c ='))

d = b ** 2 -4 * a * c

if d < 0:
    print('Thera are no real solutions')
elif d == 0:
    x1 = x2 = -b/2*a
    print(x1,x2)
else:
    x1 = (-b + sqrt(d)/ 2*a)
    x2 = (-b - sqrt(d)/ 2*a)
    print(x1,x2)