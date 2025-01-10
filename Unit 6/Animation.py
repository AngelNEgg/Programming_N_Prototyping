# Angel Nazaire
# 12/12/2024
# Period 5-6
'''Create an animation themed around winter holidays using your current knowledge of SimpleGUI and Python.'''

# ADD 2 MORE LINES
import simplegui
import random

width = 800
height = 600
Hwidth = width/2
Hheight = height/2

snowNum = 50
snowSpeed1 = 5
snowSpeed2 = 2
snowSpeed3 = 1

snowY = []


for i in range(snowNum):
    # append = assign to list
    snowY.append(random.randint(0,height))


    
def draw(canvas):
    global snowY
    # BG + Ground
    canvas.draw_polygon([(0,0),(0,height),(width,height),(width,0)], 4, "#0c1b3b", "#0c1b3b")
    canvas.draw_line((0,Hheight),(width,Hheight), 40, "#d3d9e8")
    canvas.draw_polygon([(0,Hheight),(0,height),(width,height),(width,Hheight)], 4, "#ebf1ff", "#ebf1ff")
    canvas.draw_polygon([(Hwidth,Hheight),(Hwidth/2,height),((Hwidth/2)*3,height)], 2, "#7e838f", "#7e838f")
    canvas.draw_line((Hwidth,Hheight),(Hwidth/2,height), 3, "#4f4a5c")
    canvas.draw_line((Hwidth,Hheight),((Hwidth/2)*3,height), 3, "#4f4a5c")
    
    # House (FINISH STYLE)
    canvas.draw_polygon([(Hwidth-57,Hheight),(Hwidth+57,Hheight),(Hwidth+57,Hheight+75),(Hwidth-57,Hheight+75)], 4, "#701911", "#c2451b")
    canvas.draw_polygon([(Hwidth-57,Hheight),(Hwidth+57,Hheight),(Hwidth,Hheight-75)], 4, "#596263", "#ffffff")
    
    # Filter + Moon
    canvas.draw_polygon([(0,0),(0,height),(width,height),(width,0)], 2, "rgba(82, 106, 156, 0.5)", "rgba(82, 106, 156, 0.5)")
    canvas.draw_circle((Hwidth,Hheight-150), 5, 100, "#bdbdbd", "#bdbdbd")
    canvas.draw_circle((Hwidth-25,Hheight-150), 2, 50, "#858585", "#858585")
    canvas.draw_circle((Hwidth-15,Hheight-160), 2, 50, "#858585", "#858585")
    canvas.draw_circle((Hwidth+10,Hheight-165), 2, 25, "#858585", "#858585")
    canvas.draw_circle((Hwidth,Hheight-165), 2, 25, "#858585", "#858585")
    
    # Snow
    for i in range(snowNum):
        snowX = random.randint(0,width)
        canvas.draw_circle((snowX,snowY[i]), 3, 2, "rgba(191, 212, 255, 0.25)", "rgba(255, 255, 255, 0.75)")
        snowY[i] += snowSpeed1
        if snowY[i] > height:
            snowY[i] = 0
            
    for i in range(snowNum):
        snowX1 = random.randint(0,width)
        canvas.draw_circle((snowX1,snowY[i]), 2, 1, "rgba(191, 212, 255, 0.25)", "rgba(255, 255, 255, 0.75)")
        snowY[i] += snowSpeed2
        if snowY[i] > height:
            snowY[i] = 0
            
    for i in range(500):
        snowX2 = random.randint(0,width)
        snowY2 = random.randint(0,height)
        canvas.draw_point((snowX2,snowY2), "White")

frame = simplegui.create_frame("Winter Wonderland", width, height)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
