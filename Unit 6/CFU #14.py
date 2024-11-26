#name date period

import simplegui

def draw(canvas):
    canvas.draw_line([50,10], [150,10], 4, "White")
    
    canvas.draw_line([50,20],[50,150],4,"White")

frame = simplegui.create_frame("Home", 200, 200)
frame.set_draw_handler(draw)

frame.start()
