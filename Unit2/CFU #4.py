import math

fname = input("What is your first name?")
lname = input("What is your last name?")
fulln = fname + " " + lname

print("Hello " + fulln + ", I am going to solve the quadratic formula!")

a = int(input('Enter the "A" coefficient: '))
b = int(input('Enter the "B" coefficient: '))
c = int(input('Enter the "C" coefficient: '))

d = (b**2) - (4*a*c)

x1 = (-b - (math.sqrt(d))) / (2*a)
x2 = (-b + (math.sqrt(d))) / (2*a)

print(f'The solutions are:\n\tx1 = {x1}, and x2 = {x2}.')
