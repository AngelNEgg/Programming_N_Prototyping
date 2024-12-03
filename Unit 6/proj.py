# Angel Nazaire
# 12/2/2024
# Period 5-6
'''Create a Thanksgiving themed image using your current knowledge from the "SimpleGUI" library.'''

import simplegui
import random

xmax = 600
ymax = 400
rand = random.randint(1,5)

# ymax = 2/3 of xmax

def draw(canvas):
    #BG (complete)
    def bg(canvas):
        canvas.draw_circle((xmax/2,ymax/2), xmax, xmax, "#ffaf47", "#ffaf47")
        canvas.draw_line([0,30],[xmax,30], 200, "#ff9233")
        canvas.draw_line([0,1],[xmax,1], 100, "#ff6c1c")
        canvas.draw_circle((0,0), 100, 5, "#ffbb00", "#ffe9ab")
        
        #-tree
        canvas.draw_line([0,0],[0,ymax], 50, "#634824")
        canvas.draw_line([0,0],[0,ymax], 35, "#301300")
        canvas.draw_line([-10,(ymax/2)],[(xmax/2)-200,ymax], 50, "#301300")
        
        #-sky
        canvas.draw_polygon([(50,45),(250,45),(100,15),(75,15)], 3, "rgba(255, 150, 38, 0.5)", "rgba(255, 213, 74, 0.5)")
        canvas.draw_polygon([(400,50),(550,25),(575,0),(600,0),(600,50)], 3, "rgba()", "rgba()")
    
    #ground
    def ground(canvas):
        canvas.draw_line([0,ymax],[xmax,ymax], 220, "#1A9241")
        canvas.draw_line([0,ymax],[xmax,ymax], 170, "#136D30")
        canvas.draw_circle((315,360),90,20, "#136D30", "#136D30")
        canvas.draw_circle((300,360),90,20, "#136D30", "#136D30")
        canvas.draw_line([65,295],[(xmax/2),ymax], 10, "#136D30")
        canvas.draw_line([0,303],[67,303], 26, "#136D30")
        canvas.draw_line([67,303],[(xmax/2),ymax], 26, "#136D30")
        
    
    #pumpkin (complete)
    #-stem (SHORTEN)
    def stem(canvas):
        canvas.draw_line([xmax/2,ymax/2],[xmax/2,70], 40, "Green")
        canvas.draw_line([(xmax/2)+5,ymax/2],[(xmax/2)+5,70], 35, "rgb(0,75,25)")
    
    #-shell (complete)
    def shell(canvas):
        canvas.draw_circle(((xmax/2)-40,(ymax/2)+10), 90, 4, "#B55400", "#FFAB00")
        canvas.draw_circle(((xmax/2)+40,(ymax/2)+10), 90, 4, "#B55400", "#FFAB00")
        canvas.draw_circle((xmax/2,ymax/2), 100, 5, "#B55400", "#FFAB00")
    
    #-overlay (complete)
    def shade(canvas):
        #-shading
        canvas.draw_circle(((xmax/2)+5,(ymax/2)+6), 95, 5, "rgba(0,0,0,0)", "#AD7400")
        canvas.draw_circle(((xmax/2)-40,(ymax/2)+16), 85, 4, "rgba(0,0,0,0)", "#AD7400")
        canvas.draw_circle((((xmax/2)+45,(ymax/2)+16)), 85, 4, "rgba(0,0,0,0)", "#AD7400")
        
        #-darker
        canvas.draw_circle(((xmax/2)+5,(ymax/2)+16), 85, 5, "rgba(0,0,0,0)", "#824800")
        canvas.draw_circle(((xmax/2)-42,(ymax/2)+26), 75, 4, "rgba(0,0,0,0)", "#824800")
        canvas.draw_circle((((xmax/2)+47,(ymax/2)+26)), 75, 4, "rgba(0,0,0,0)", "#824800")
        
        #-particles
        for i in range(1,1000):
            
            r = random.randint(0,255)
            g = random.randint(105,125)
            b = 0

            randRGBColor = "RGB( " + str(r) + "," + str(g) + "," + str(b) + ")"     

            x = random.randint(2, xmax)
            y = random.randint(2, xmax)

            canvas.draw_point((x, y), randRGBColor)
        
        #-leaves (RANDOM) (REWRITE)
        for i in range(1,100):
            
            r = random.randint(0,255)
            g = random.randint(105,125)
            b = 0

            randRGBColor = "RGB( " + str(r) + "," + str(g) + "," + str(b) + ")"     

            x = random.randint(2, xmax)
            y = random.randint(2, xmax)

            canvas.draw_polygon((x, y), randRGBColor)
         
        
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
