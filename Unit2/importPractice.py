import math

r = int(input("What is the radius of your circle?"))
c = 2*r*math.pi
a = math.pi*r**2

print("C=" ,c," A=" ,a)
-----------------------------------------------------------------------
import math

#r = radius, h = height
r = int(input("What is the radius of your cylinder?"))
h = int(input("What is the height of your cylinder?"))

#v = volume
v = math.pi*r**2*h

print("The volume of your cylinder is",v)
