#name date period

import simplegui

# 33.3333333333

num = 10

def draw_handler(canvas,x1,x2,y):
    #all drawing is here
    # canvas.draw_point([x,y],"color")
    
    canvas.draw_point([x1,y],"White")
    canvas.draw_point([x2,y],"White")
    y += 1
    if y == 5:
        pass
    else:
        draw_handler(canvas,x1,x2,y)
    

# library.create_frame("name of canvas", width, height)

frame = simplegui.create_frame("CFU #13: Happy Dots", 200, 200)
frame.set_canvas_background("Black")
frame.set_draw_handler(draw_handler(frame,one,five,num))
frame.start()
