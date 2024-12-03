# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

#ffe9ab


# Angel Nazaire
# 12/2/2024
# Period 5-6

import simplegui
import random

xmax = 600
ymax = 400

# ymax = 2/3 of xmax

def draw(canvas):
    #BG (SCALE GRADIENT)
    def bg(canvas):
        canvas.draw_circle((xmax/2,ymax/2), xmax, xmax, "#ffaf47", "#ffaf47")
        canvas.draw_line([0,30],[xmax,30], 100, "#ff9233")
        canvas.draw_line([0,1],[xmax,1], 50, "#ff6c1c")
        canvas.draw_circle((0,0), 50, 5, "#ffbb00", "#ffe9ab")
    
    #ground
    def ground(canvas):
        canvas.draw_line([0,ymax],[xmax,ymax], 220, "#1A9241")
        canvas.draw_line([0,ymax],[xmax,ymax], 170, "#136D30")
    
    #pumpkin (MOVE DOWN TO GROUND)
    #-stem (SHORTEN)
    def stem(canvas):
        canvas.draw_line([xmax/2,ymax/2],[xmax/2,30], 40, "Green")
        canvas.draw_line([(xmax/2)+5,ymax/2],[(xmax/2)+5,30], 35, "rgb(0,75,25)")
    
    #-shell (REPOSITION)
    def shell(canvas):
        canvas.draw_circle(((xmax/2)-40,(ymax/2)+10), 90, 4, "#B55400", "#FFAB00")
        canvas.draw_circle(((xmax/2)+40,(ymax/2)+10), 90, 4, "#B55400", "#FFAB00")
        canvas.draw_circle((xmax/2,ymax/2), 100, 5, "#B55400", "#FFAB00")
    
    #-shading (complete)
    def shade(canvas):
        canvas.draw_circle(((xmax/2)+5,(ymax/2)+6), 95, 5, "rgba(0,0,0,0)", "#AD7400")
        canvas.draw_circle(((xmax/2)-40,(ymax/2)+16), 85, 4, "rgba(0,0,0,0)", "#AD7400")
        canvas.draw_circle((((xmax/2)+45,(ymax/2)+16)), 85, 4, "rgba(0,0,0,0)", "#AD7400")
        #-darker
        canvas.draw_circle(((xmax/2)+5,(ymax/2)+16), 85, 5, "rgba(0,0,0,0)", "#824800")
        canvas.draw_circle(((xmax/2)-42,(ymax/2)+26), 75, 4, "rgba(0,0,0,0)", "#824800")
        canvas.draw_circle((((xmax/2)+47,(ymax/2)+26)), 75, 4, "rgba(0,0,0,0)", "#824800")
        
        #-leaves (RANDOM) (IMPLEMENT)
        
        #-filter (complete)
        canvas.draw_circle((xmax/2,ymax/2), xmax, xmax, "rgba(135,72,0,0)", "rgba(135,72,0,0.25)")
    
    bg(canvas)
    ground(canvas)
    stem(canvas)
    shell(canvas)
    shade(canvas)

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", xmax, ymax)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
