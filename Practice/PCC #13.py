# Angel Nazaire
# 3/28/2025
# Period 5-6

import turtle
import math

def forward(x,y):
  turtle.Turtle.forward(x,y)
def left(x,y):
  turtle.Turtle.left(x,y)
def right(x,y):
  turtle.Turtle.right(x,y)
def back(x,y):
  turtle.Turtle.back(x,y)
  
def triIso(t,r,angle):
   y = r*math.sin(math.radians(angle))
   right(t,angle)
   forward(t,r)
   left(t,90+angle)
   forward(t,y*2)
   left(t,90+angle)
   forward(t,r)
   left(t,180-angle)
  
  
def pie(t,n,r):
  angle = 360/n
  for i in range(n):
    triIso(t,r,angle/2)
    left(t,angle)
  
def draw_pies(t,n,r):
  pie(t, n, r)
  t.pu()
  forward(t,75)
  t.pd()

david = turtle.Turtle()
david.shape("turtle")
david.speed(5)
david.color("Green")

draw_pies(david, 5, 25)
draw_pies(david, 6, 25)
draw_pies(david, 7, 25)
