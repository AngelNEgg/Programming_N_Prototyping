# Angel Nazaire
# 11/27/2024
# Period 5-6
# Create a smiley-face using only 'canvas.create_circle()'

import simplegui

def draw(canvas):
    #BG
    canvas.draw_circle([150,150],400 , 400, "White", "White")
    
    #Head
    canvas.draw_circle([150,150], 50, 100, "rgb(255,255,0)")
    canvas.draw_circle([150,150], 100, 10, "rgb(255,155,25)")
    
    #Nose
    canvas.draw_circle([150,150], 5, 10, "rgb(255,165,0)")
    canvas.draw_circle([150,146], 5, 10, "rgb(255,255,0)")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Test", 300, 300)
frame.set_draw_handler(draw)


# Start the frame animation
frame.start()
