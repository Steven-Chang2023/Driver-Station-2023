import button
from tkinter import Tk, PhotoImage, Canvas, CENTER, RIGHT, LEFT
import math
#from PIL import Image, ImageTk
import os

dirname = os.path.dirname(__file__)

test = False

if test:
    import fakeSerial as serial
else:
    import serial


ser = serial.Serial("/dev/ttyAMA0", 9600)  # /dev/ttyAMA0 on the pi

root = Tk()
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
btnW = 250
btnH = 100
btnX = 510
btnY = 95
padding = 30
color_inactive = "white"
color_active = "green"

# Delay between pushes (ms)
delay = 10

# Button Dimensions and button objects
bNeutral = button.Button('btnN', 130, btnY  + btnH + padding, btnW, btnH, "neutral", color_inactive)
b1 = button.Button('btn1', btnX, btnY, btnW, btnH, "low", color_inactive)
b2 = button.Button('btn2', btnX, btnY + btnH + padding,
                   btnW, btnH, "middle", color_inactive)
b3 = button.Button('btn3', btnX, btnY + (btnH + padding)
                   * 2, btnW, btnH, "high", color_inactive)

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
    ex.checkClicked(event)
    if (b1.isClicked):
        b1.color = color_active
        b2.color = color_inactive
        b3.color = color_inactive
        bNeutral.color = color_inactive
    elif (b2.isClicked):
        b1.color = color_inactive
        b2.color = color_active
        b3.color = color_inactive
        bNeutral.color = color_inactive
    elif (b3.isClicked):
        b1.color = color_inactive
        b2.color = color_inactive
        b3.color = color_active
        bNeutral.color = color_inactive
    elif (bNeutral.isClicked):
        bNeutral.color = color_active
        b1.color = color_inactive
        b2.color = color_inactive
        b3.color = color_inactive
    elif (ex.isClicked):
        exit()
    else:
        b1.color = color_inactive
        b2.color = color_inactive
        b3.color = color_inactive
    drawStuff()


def drawStuff():
    # Draw different Starting Positions
    bNeutral.drawButton(ctx)
    b1.drawButton(ctx)
    b2.drawButton(ctx)
    b3.drawButton(ctx)
    ex.drawButton(ctx)


drawStuff()

ctx.bind("<Button-1>", handle_click)
ctx.pack()


def publish():
    if (b1.isClicked):
        ser.write(b'\x01')
    elif (b2.isClicked):
        ser.write(b'\x02')
    elif (b3.isClicked):
        ser.write(b'\x03')
    elif (bNeutral.isClicked):
         print("zamn")
    root.after(delay, publish)


root.after(delay, publish)
root.mainloop()
