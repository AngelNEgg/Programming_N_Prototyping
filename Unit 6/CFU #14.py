#name date period

import simplegui

def draw_handler(canvas):
    

# library.create_frame("name of canvas", width, height)

frame = simplegui.create_frame("CFU #13: Happy Dots", 200, 200)
frame.set_canvas_background("Black")
frame.set_draw_handler(draw_handler(frame,one,five,num))
frame.start()
