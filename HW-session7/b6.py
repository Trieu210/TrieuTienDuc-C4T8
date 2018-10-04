sides = int(input("Enter the number of sides u want"))
angle = 360 / sides

from turtle import *
for i in range (sides):
    forward(50)
    left(angle)

mainloop()

