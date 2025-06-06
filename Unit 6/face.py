import simplegui

xmax = 200
ymax = 200

def draw(canvas):
    canvas.draw_circle((xmax/2,ymax/2), 75, 10, "#fcb503", "#fcd703")
    canvas.draw_circle((xmax/2-25,ymax/2-25), 5, 10, "Black")
    canvas.draw_circle((xmax/2+25,ymax/2-25), 5, 10, "Black")
    canvas.draw_line((xmax/2-25,ymax/2+25),(xmax/2+25,ymax/2+25), 5, "brown")

frame = simplegui.create_frame("Home", xmax, ymax)
frame.set_draw_handler(draw)

frame.start()
