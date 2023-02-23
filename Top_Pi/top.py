import button
from tkinter import Tk, Canvas, CENTER, RIGHT, LEFT, N, PhotoImage
import math
import os

dirname = os.path.dirname(__file__)

test = True

if test:
    import fakeSerial as serial
else:
    import serial


ser = serial.Serial("/dev/ttyAMA0", 9600)  # /dev/ttyAMA0 on the pi

root = Tk()
# Full screen
# Full screen
if not test:
    root.overrideredirect(True)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(),
                                       root.winfo_screenheight()))
    root.focus_set()  # Move focus to this widget
    root.bind("<Escape>", lambda e: root.quit())
    root.config(cursor="none")

# Variables
height = 480
width = 800
btnW = 130
btnH = 100
btnX = 420
btnY = 80
padding = 40
color_inactive = "white"
color_active = "green"

# Delay between pushes (ms)
delay = 10

# Button Dimensions and button objects
bNeutral = button.Button('btnN', 80, btnY  + btnH + padding, btnW, btnH, "neutral", color_inactive)
b1 = button.Button('btn1', btnX-(btnW + padding), btnY, btnW, btnH, "1", color_inactive)
b2 = button.Button('btn2', btnX-(btnW + padding), btnY + btnH + padding,
                   btnW, btnH, "2", color_inactive)
b3 = button.Button('btn3', btnX-(btnW + padding), btnY + (btnH + padding)
                   * 2, btnW, btnH, "3", color_inactive)
b4 = button.Button('btn4', btnX, btnY, btnW, btnH, "4", color_inactive)
b5 = button.Button('btn5', btnX, btnY + btnH + padding,
                   btnW, btnH, "5", color_inactive)
b6 = button.Button('btn6', btnX, btnY + (btnH + padding)
                   * 2, btnW, btnH, "6", color_inactive)
b7 = button.Button('btn7', btnX+(btnW + padding), btnY, btnW, btnH, "7", color_inactive)
b8 = button.Button('btn8', btnX+(btnW + padding), btnY + btnH + padding,
                   btnW, btnH, "8", color_inactive)
b9 = button.Button('btn9', btnX+(btnW + padding), btnY + (btnH + padding)
                   * 2, btnW, btnH, "9", color_inactive)

buttonArray = [b1,b2,b3,b4,b5,b6,b7,b8,b9,bNeutral]
# Exit button - top left
ex = button.Button('exit', 0, 0, 25, 25, "X", "red")

# Canvas object
ctx = Canvas(root, width=width, height=height, background="black")
ctx.pack()

# Background
#bg = Image.open(os.path.join(dirname, './field.png'))
#bg = ImageTk.PhotoImage(bg)
#ctx.create_image(width/2, height/2, anchor=CENTER, image=bg)

# Text at top
ctx.create_text(400, 25, justify=CENTER, text="Choose a starting position", font=(
    "Arial", 28), fill="White")


def handle_click(event):
    if not test:
        event.x = math.fabs(event.x-800)
        event.y = math.fabs(event.y-480)

    # If any of the buttons are clicked, theere is a new line saying "selected"
    # and set the others to the position name, otherwise set them all to the position
    bNeutral.checkClicked(event)
    b1.checkClicked(event)
    b2.checkClicked(event)
    b3.checkClicked(event)
    b4.checkClicked(event)
    b5.checkClicked(event)
    b6.checkClicked(event)
    b7.checkClicked(event)
    b8.checkClicked(event)
    b9.checkClicked(event)
    ex.checkClicked(event)
    for but in buttonArray:
        if(but.isClicked):
            but.color = color_active
        else:
            but.color = color_inactive
    
    if (ex.isClicked):
        exit()
    
    
    
    drawStuff()


def drawStuff():
    # Draw different Starting Positions
    bNeutral.drawButton(ctx)
    ex.drawButton(ctx)
    for button in buttonArray:
        button.drawButton(ctx)


drawStuff()

ctx.bind("<Button-1>", handle_click)
ctx.pack()


def publish():
    if (b1.isClicked):
        print(1)
    elif (b2.isClicked):
        print(2)
    elif (b3.isClicked):
        print(3)
    elif (b4.isClicked):
        print(4)
    elif (b5.isClicked):
        print(5)
    elif (b6.isClicked):
        print(6)
    elif (b7.isClicked):
        print(7)
    elif (b8.isClicked):
        print(8)
    elif (b9.isClicked):
        print(9)
    elif(bNeutral.isClicked):
        print("zamn")
    
    root.after(delay, publish)


root.after(delay, publish)
root.mainloop()
