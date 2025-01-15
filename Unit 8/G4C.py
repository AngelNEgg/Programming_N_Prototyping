# Angel Nazaire
# 1/14/2025
# Period 5-6
'''Games4Change Final Project: Peaceformers Game'''

import simplegui

width = 600
height = 600

message = "Welcome!"
player = simplegui.load_image("https://i.ibb.co/FmY1Rzx/pixil-frame-0.png")
floor = simplegui.load_image("https://i.ibb.co/B4tMr5h/pixil-frame-0.png")
P_WIDTH = 32
P_HEIGHT = 32
F_WIDTH = 150
F_HEIGHT = 150
posX = width/2
posY = height/2
debug = "placeholder"

# Handler for mouse


# Handler for keys
def keydown(key):
    global debug
    global posX
    global posY
    ####### Add KEY_MAP to translate to key codes
    if key == simplegui.KEY_MAP["up"]:
        debug = "Up arrow"
        posY -= 20
    elif key == simplegui.KEY_MAP["down"]:
        debug = "Down arrow"
        posY += 20
    elif key == simplegui.KEY_MAP["left"]:
        debug = "Left arrow"
        posX -= 20
    elif key == simplegui.KEY_MAP["right"]:
        debug = "Right arrow"
        posX += 20
    elif key == simplegui.KEY_MAP["space"]:
        debug = "Spacebar"

# Handler to draw on canvas
def draw(canvas):
    # Scene (**ADD OBJECTS)
    #canvas.draw_polygon([(width/4,height/4), ((width/4)*3,height/4), ((width/4)*3,(height/4)*3), (width/4,(height/4)*3)], 1, "Black", "Brown") reference square for floor texture size
    canvas.draw_image(floor, (F_WIDTH/2, F_HEIGHT/2),(F_WIDTH, F_HEIGHT), (300, 300), (300, 300))
    
    # Player (DRAW LAST)
    canvas.draw_image(player, (P_WIDTH / 2, P_HEIGHT / 2), (P_WIDTH, P_HEIGHT), (posX, posY), (50, 50))

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", width, height)
frame.add_label("Click the screen to start!")
frame.add_label("Use the arrow keys to move!")
frame.set_keydown_handler(keydown)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
