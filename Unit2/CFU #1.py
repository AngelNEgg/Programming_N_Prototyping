import math

fname = input("What is your first name?")
lname = input("What is your last name?")
fulln = fname + " " + lname

print("Hello " + fulln + ", I am going to solve the quadratic formula!")

a = int(input('Enter the "A" coefficient: '))
b = int(input('Enter the "B" coefficient: '))
c = int(input('Enter the "C" coefficient: '))

p1 = b**2
p2 = 4*a*c
p3 = 2*a
p4 = p1 - p2
p5 = math.sqrt(p4)

x1 = (-b - p5)/p3
x2 = (-b + p5)/p3

quad = (a(x1))**2+b(x2)-c
