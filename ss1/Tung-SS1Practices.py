# -*- coding: utf-8 -*-
"""
Created on Thu May 14 10:38:40 2020

@author: Tung Linh
"""
"""
to check variable's type:
    print(type(Variable))
several invalid variable names:
    - 345variable
    - variable%*&^&(
    - print
"""
"""
# area of a circle:
Radius = int(input("Radius? "))
Area = 3.14 * (Radius**2)
print("Area = ",str(Area))

# Conversion of Temperature:
Cel = int(input("Enter the temperature in Celsius? "))
Fah = Cel * 9 / 5 + 32
print(Cel," (C) = ",Fah," (F)")
"""

# setting turtle:
from turtle import *
speed(-1)
color('orange')

"""
# square:
begin_fill()
for edge in range(4):
    forward(100)
    left(90)
end_fill()

# triangle:
begin_fill()
for edge in range(3):
    forward(100)
    left(120)
end_fill()

# circle :
begin_fill()
Radius = 50
circle(Radius)
end_fill()

# multi circle:
Radius = 50
loops = 6
for loop in loops:
    circle(Radius)
    left(360/loops)
"""
# multi circle:
Radius = 50
loops = int(input("num of circles? "))
for loop in range(loops):
    circle(Radius)
    left(360/loops)
mainloop()