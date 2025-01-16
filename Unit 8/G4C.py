# Angel Nazaire
# 1/14/2025
# Period 5-6
'''Games4Change Final Project: Peaceformers Game'''

''' SimpleGUI File URL functions (always load into variable first):
Images: canvas.draw_image((half width, half height), (width, height),(x on frame, y on frame),(x scale, y scale))'''

import simplegui

# Frame aspect ratio
width = 600
height = 600

# Sprites
player = simplegui.load_image("https://i.ibb.co/FmY1Rzx/pixil-frame-0.png")
floor = simplegui.load_image("https://i.ibb.co/B4tMr5h/pixil-frame-0.png")
enemy = simplegui.load_image("https://i.ibb.co/KKhRfpS/pixil-frame-0-1.png")

# Sprite aspect ratios
## Player
P_WIDTH = 32
P_HEIGHT = 32
## Enemy
E_WIDTH = 32
E_HEIGHT = 32
## Floor Texture
F_WIDTH = 150
F_HEIGHT = 150

# Player position vars
posX = width/2
posY = height/2

# Misc.
health = 100
print(f"Health: {health}")
debug = "placeholder"
test = [posX,posY]
## Hurtsound may not work (prepare backup)
hurtsound = simplegui.load_sound("https://www.myinstants.com/en/instant/undertale-damage-taken/?utm_source=copy&utm_medium=share")

# Handler for keys
def keydown(key):
    global debug
    global posX
    global posY
    global health
    # Key detection (COMPLETE)
    if key == simplegui.KEY_MAP["up"]:
        debug = "Up arrow"
        posY -= 20
    elif key == simplegui.KEY_MAP["down"]:
        debug = "Down arrow"
        posY += 20
    elif key == simplegui.KEY_MAP["left"]:
        debug = "Left arrow"
        posX -= 20
    elif key == simplegui.KEY_MAP["right"]:
        debug = "Right arrow"
        posX += 20
    elif key == simplegui.KEY_MAP["space"]:
        debug = "Spacebar"
        
# Enemy detection (BUGGED)
if posX == 340 and posY == 340 and debug == "Right arrow":
    health -= 10
    heal.set_text(f"Health: {health}")
    hurtsound.play()
    posX -= 20
    if health < 1:
        print("GAME OVER")
elif posX == 340 and posY == 340 and debug == "Left arrow":
    health -= 10
    heal.set_text(f"Health: {health}")
    hurtsound.play()
    posX += 20
    if health < 1:
        print("GAME OVER")
elif posX == 340 and posY == 340 and debug == "Up arrow":
    health -= 10
    heal.set_text(f"Health: {health}")
    hurtsound.play()
    posY += 20
    if health < 1:
        print("GAME OVER")
elif posX == 340 and posY == 340 and debug == "Down arrow":
    health -= 10
    heal.set_text(f"Health: {health}")
    hurtsound.play()
    posY -= 20
    if health < 1:
        print("GAME OVER")

# Handler to draw on canvas
def draw(canvas):
    # Scene (**ADD OBJECTS)
    #canvas.draw_polygon([(width/4,height/4), ((width/4)*3,height/4), ((width/4)*3,(height/4)*3), (width/4,(height/4)*3)], 1, "Black", "Brown") reference square for floor texture size
    canvas.draw_image(floor, (F_WIDTH/2, F_HEIGHT/2),(F_WIDTH, F_HEIGHT), (300, 300), (300, 300))
    
    # Characters (DRAW LAST)
    canvas.draw_image(player, (P_WIDTH / 2, P_HEIGHT / 2), (P_WIDTH, P_HEIGHT), (posX, posY), (50, 50))
    canvas.draw_image(enemy, (E_WIDTH / 2, E_HEIGHT / 2), (E_WIDTH, E_HEIGHT), (340, 340), (50, 50))

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", width, height)
frame.set_canvas_background("DodgerBlue")
frame.add_label("Click the screen to start!")
frame.add_label("Use the arrow keys to move!")
heal = frame.add_label(f"{health}")
heal.set_text(f"Health: {health}")
frame.set_keydown_handler(keydown)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
