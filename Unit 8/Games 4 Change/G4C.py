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
grass = simplegui.load_image("https://i.ibb.co/wMhQWFt/pixil-frame-0-2.png")
resource = simple.load_image("")

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
## Grass Texture
G_WIDTH = width
G_HEIGHT = height
## Resource
R_WIDTH
R_HEIGHT

# Player position vars
posX = width/2
posY = height/2
position = (posX,posY)

# Misc.
health = 100
print("Game Start")
debug = "placeholder"
test = [posX,posY]
## Hurtsound may not work (no headphones to test)
hurtsound = simplegui.load_sound("https://www.myinstants.com/en/instant/undertale-damage-taken/?utm_source=copy&utm_medium=share")

# Handler for player logic
def keydown(key):
    global debug
    global posX
    global posY
    global health
    
    if health == 0:
        pass
    else:
        
        ## Key detection (COMPLETE)
        if key == simplegui.KEY_MAP["up"]:
            debug = "Up arrow"
            print("Player went Up")
            posY -= 20
        elif key == simplegui.KEY_MAP["down"]:
            debug = "Down arrow"
            print("Player went Down")
            posY += 20
        elif key == simplegui.KEY_MAP["left"]:
            debug = "Left arrow"
            print("Player went Left")
            posX -= 20
        elif key == simplegui.KEY_MAP["right"]:
            debug = "Right arrow"
            print("Player went Right")
            posX += 20
        elif key == simplegui.KEY_MAP["space"]:
            print("Player pressed Space")
            debug = "Spacebar"
        if key == simplegui.KEY_MAP["space"] and (posX >= 320 and posX < 380) and (posY <= 360 and posY > 300):
            print("success")

        ## Enemy detection (Fixed)
        ### Player Damage (COMPLETE)
        if posX == 340 and posY == 340 and debug == "Right arrow":
            print("Ouch!")
            health -= 10
            heal.set_text(f"Health: {health}")
            hurtsound.play()
            posX -= 20
            if health < 1:
                print("\nGAME OVER")
                print("Reset and try again!")
        elif posX == 340 and posY == 340 and debug == "Left arrow":
            print("Ouch!")
            health -= 10
            heal.set_text(f"Health: {health}")
            hurtsound.play()
            posX += 20
            if health < 1:
                print("\nGAME OVER")
                print("Reset and try again!")
        elif posX == 340 and posY == 340 and debug == "Up arrow":
            print("Ouch!")
            health -= 10
            heal.set_text(f"Health: {health}")
            hurtsound.play()
            posY += 20
            if health < 1:
                print("\nGAME OVER")
                print("Reset and try again!")
        elif posX == 340 and posY == 340 and debug == "Down arrow":
            print("Ouch!")
            health -= 10
            heal.set_text(f"Health: {health}")
            hurtsound.play()
            posY -= 20
            if health < 1:
                print("\nGAME OVER")
                print("Reset and try again!")
        
# Handler to draw on canvas
def draw(canvas):
    # Scene (**ADD OBJECTS)
    canvas.draw_image(grass, (G_WIDTH/2, G_HEIGHT/2), (G_WIDTH, G_HEIGHT), (300,300), (600,600))
    canvas.draw_polygon([(width/4,height/4), ((width/4)*3+5,height/4+5), ((width/4*3)+5,(height/4*3)+5), (width/4,(height/4)*3)], 1, "rgba(0,0,0,0)", "rgba(0,100,25,0.5)")
    canvas.draw_image(floor, (F_WIDTH/2, F_HEIGHT/2),(F_WIDTH, F_HEIGHT), (300, 300), (300, 300))
    
    # Characters (DRAW LAST)
    canvas.draw_circle((posX+5,posY+5), 15, 1, "rgba(0,0,0,0)", "rgba(0,0,0,0.25)")
    canvas.draw_image(player, (P_WIDTH / 2, P_HEIGHT / 2), (P_WIDTH, P_HEIGHT), (posX, posY), (50, 50))
    canvas.draw_circle((340+5,340+5), 15, 1, "rgba(0,0,0,0)", "rgba(0,0,0,0.25)")
    canvas.draw_image(enemy, (E_WIDTH / 2, E_HEIGHT / 2), (E_WIDTH, E_HEIGHT), (340, 340), (50, 50))

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", width, height)
frame.set_canvas_background("DodgerBlue")
frame.add_label("Click the screen to start!")
frame.add_label("Use the arrow keys to move!")
frame.add_label("Press space to teach the enemy how to share! (Don't get too close!)")
heal = frame.add_label(f"{health}")
heal.set_text(f"Health: {health}")
frame.set_keydown_handler(keydown)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
