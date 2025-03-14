import turtle

def forward(x,y):
  turtle.Turtle.forward(x,y)
def left(x,y):
  turtle.Turtle.left(x,y)
def right(x,y):
  turtle.Turtle.right(x,y)
def back(x,y):
  turtle.Turtle.back(x,y)
  
def draw_frac(t,length,n):
    if n == 0:
      return
    angle = 50
    forward(t,length*n)
    left(t,angle)
    draw_frac(t, length, n-1)
    right(t,2*angle)
    draw_frac(t, length, n-1)
    left(t,angle)
    back(t,length*n)

def draw_square(t,length,n):
  if n == 0:
    return
  angle = 90
  forward(t,length)
  left(t,angle)
  draw_square(t, length, n-1)
  
  
tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.speed(3.5)
tommy.color("Green")

bob = turtle.Turtle()
bob.shape("turtle")
bob.speed(2)
bob.color("Red")

draw_frac(tommy, 10, 5)
draw_square(bob, 40, 4)
