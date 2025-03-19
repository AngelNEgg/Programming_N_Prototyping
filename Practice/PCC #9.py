import turtle

def forward(x,y):
  turtle.Turtle.forward(x,y)
def left(x,y):
  turtle.Turtle.left(x,y)
def right(x,y):
  turtle.Turtle.right(x,y)
def back(x,y):
  turtle.Turtle.back(x,y)
  
def draw_square1(t,length,n):
    if n == 0:
      return
    angle = 90
    forward(t,length)
    left(t,angle)
    draw_square1(t, length, n-1)

def draw_square2(t,length,n):
  if n == 0:
    return
  angle = 90
  forward(t,length)
  left(t,angle)
  draw_square2(t, length, n-1)
  
def draw_square3(t,length,n):
  if n == 0:
    return
  angle = 45
  forward(t,length)
  left(t,angle)
  draw_square3(t, length, n-1)
  
  
tommy = turtle.Turtle()
tommy.shape("turtle")
tommy.speed(3.5)
tommy.color("Green")

bob = turtle.Turtle()
bob.shape("turtle")
bob.speed(2)
bob.color("Red")

shelly = turtle.Turtle()
shelly.shape("turtle")
shelly.speed(2)
shelly.color("Blue")

draw_square1(tommy, 40, 5)
draw_square2(bob, 80, 4)
draw_square3(shelly,80,8)
