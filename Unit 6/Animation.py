# Angel Nazaire
# 12/12/2024
# Period 5-6
'''Create an animation themed around winter holidays using your current knowledge of SimpleGUI and Python.'''


import simplegui
import random

width = 600
height = 400
Hwidth = width/2
Hheight = height/2

snowNum = 5
snowSpeed = 30

snowY = []

for i in range(snowNum):
    # append = assign to list
    snowY.append(random.randint(0,height))


    
def draw(canvas):
    global snowY
    # BG + Ground
    canvas.draw_polygon([(0,0),(0,height),(width,height),(width,0)], 4, "#0c1b3b", "#0c1b3b")
    canvas.draw_polygon([(0,Hheight),(0,height),(width,height),(width,Hheight)], 4, "rgb(191, 212, 255)", "rgb(191, 212, 255)")
    
    # House (SET POSITION)
    canvas.draw_polygon([(),(),(),()], 2, "#c2451b", "#c2451b")
    
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
