# Angel Nazaire
# 12/12/2024
# Period 5-6
'''Create an animation themed around winter holidays using your current knowledge of SimpleGUI and Python.'''

# Road color: #7e838f
import simplegui
import random

width = 600
height = 400
Hwidth = width/2
Hheight = height/2

snowNum = 50
snowSpeed = 1

snowY = []

for i in range(snowNum):
    # append = assign to list
    snowY.append(random.randint(0,height))


    
def draw(canvas):
    global snowY
    # BG + Ground
    canvas.draw_polygon([(0,0),(0,height),(width,height),(width,0)], 4, "#0c1b3b", "#0c1b3b")
    canvas.draw_polygon([(0,Hheight),(0,height),(width,height),(width,Hheight)], 4, "#ebf1ff", "#ebf1ff")
    canvas.draw_polygon([(Hwidth,Hheight),(Hwidth/2,height),((Hwidth/2)*3,height)], 2, "#7e838f", "#7e838f")
    
    # House (FINISH STYLE)
    canvas.draw_polygon([(Hwidth-57,Hheight),(Hwidth+57,Hheight),(Hwidth+57,Hheight+75),(Hwidth-57,Hheight+75)], 4, "#701911", "#c2451b")
    canvas.draw_polygon([(Hwidth-57,Hheight),(Hwidth+57,Hheight),(Hwidth,Hheight-75)], 4, "#596263", "#ffffff")
    
    # Filter
    canvas.draw_polygon([(0,0),(0,height),(width,height),(width,0)], 2, "rgba(82, 106, 156, 0.5)", "rgba(82, 106, 156, 0.5)")
    
    # Snow
    for i in range(snowNum):
        snowX = random.randint(0,width)
        canvas.draw_circle((snowX,snowY[i]), 3, 2, "rgba(191, 212, 255, 0.25)", "rgba(255, 255, 255, 0.75)")
        snowY[i] += snowSpeed
        if snowY[i] > height:
            snowY[i] = 0

frame = simplegui.create_frame("Winter Wonderland", width, height)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
