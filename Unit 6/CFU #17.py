#Angel Nazaire
#12/6/2024
#Period 5-6

'''Sample code for scaling images'''

import simplegui

#frame width
xmax = int(imput("Width of canvas: "))

#frame height
ymax = int(imput("height of canvas: "))

#Shape visibility toggles
show_shape1 = True
show_shape2 = True
show_shape3 = True
show_shape4 = True

# 'None' sets the frame to a global (not specific) reference
frame = None

#toggle all shapes
def all_shapes():
  global shape, shape2
  shape1 = shape2 = False
  
#toggle first shape
def shape_one():
    global show_shape
    
#draw a shape in one quadrant
def draw_triangle(canvas,cx,cy,size):
  half_size = size / 2
  canvas.draw_polygon([(cx,cy - half_size), (cx-half_size,cy+half_size), (cx+half_size,cy+half_size)], 2, "Blue", "Blue")

def draw(canvas):
  quadX = xmax / 2
  quadY = ymax / 2
  draw_triangle(canvas, (quadX / 2), (ymax - quadY), 100)

#frame
def create_frame():
  global frame
  frame = simplegui.create_frame("CFU #17", xmax, ymax)
  frame.set_canvas_background("Green")
  frame.set_draw_handler(draw)
  frame.start() 
  
create_frame()
