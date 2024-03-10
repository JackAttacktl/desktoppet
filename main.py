import pyautogui
import random
import tkinter as tk
from PIL import Image, ImageTk
from time import time
import math

screenSize = pyautogui.size()

petX = screenSize.width//2
petY = 0
petVelX = 0
petVelY = 0
petDragging = False

petLastX = 0
petLastY = 0

petState = 0
petStateLastSwitch = time()

lastTick = time()

def update():
    global petX
    global petY
    global petVelX
    global petVelY
    global lastTick
    global screenSize
    global petDragging
    global petLastX
    global petLastY
    global petState
    global petStateLastSwitch
    delta = time() - lastTick
    lastTick = time()
    mouseX,mouseY = window.winfo_pointerxy()
    window.geometry('100x100+{}+{}'.format(round(petX),round(petY)))
    if (not petDragging):
        if (petY < screenSize.height - 100):
            petVelY += delta * 1000
        else:
            petVelY = abs(petVelY) * -0.2
            petY = screenSize.height - 100
        
        if (round(petY + 100) >= screenSize.height):
            petVelX *= 0.98
        else:
            petVelX *= 0.999
        
        if (petY < 0):
            petVelY = abs(petVelY) * 0.2
            petY = 0
        
        if (petX > screenSize.width - 100):
            petVelX = abs(petVelX) * -0.2
            petX = screenSize.width - 100

        if (petX < 0):
            petVelX = abs(petVelX) * 0.2
            petX = 0


        petX += petVelX * delta
        petY += petVelY * delta
    else:
        petStateLastSwitch = time()
        petState = 0
        petX = mouseX - 50
        petY = mouseY - 50
        petVelX = (petX - petLastX) * 100
        petVelY = (petY - petLastY) * 100
    petLastX += (petX - petLastX) * delta * 100
    petLastY += (petY - petLastY) * delta * 100
    # State Evaluation
    if (petState == 0):
        if (random.random() <= 0.001 and (time() - petStateLastSwitch) > 3):
            if (random.random() <= 0.5):
                print('state 1')
                petState = 1
            else:
                print('state 2')
                petState = 2
            petStateLastSwitch = time()
        elif (random.random() <= 0.001 and (time() - petStateLastSwitch) > 3):
            print('state 3')
            petState = 3
            petStateLastSwitch = time()
        elif (random.random() <= 0.001 and (time() - petStateLastSwitch) > 3):
            if (random.random() <= 0.5):
                print('state 4')
                petState = 4
            else:
                print('state 5')
                petState = 5
            petStateLastSwitch = time()
    elif (petState == 1):
        petX += 100 * delta
        if (random.random() <= 0.001 and (time() - petStateLastSwitch) > 3):
            print('state 0')
            petStateLastSwitch = time()
            petState = 0
        if (petX > screenSize.width - 100):
            petState = 2
            print('Turning around')
    elif (petState == 2):
        petX -= 100 * delta
        if (random.random() <= 0.001 and (time() - petStateLastSwitch) > 3):
            print('state 0')
            petStateLastSwitch = time()
            petState = 0
        if (petX < 0):
            petState = 1
            print('Turning around')
    elif (petState == 3):
        if (random.random() <= 0.001 and (time() - petStateLastSwitch) > 2):
            print('state 0')
            petStateLastSwitch = time()
            petState = 0
        if (round(petY) >= screenSize.height - 100):
            petVelY = -300
    elif (petState == 4):
        if (random.random() <= 0.001 and (time() - petStateLastSwitch) > 2):
            print('state 0')
            petStateLastSwitch = time()
            petState = 0
        if (round(petY) >= screenSize.height - 100):
            petVelY = -300
            petVelX = 300
            petState = 5
            petY = screenSize.height - 101
    elif (petState == 5):
        if (random.random() <= 0.001 and (time() - petStateLastSwitch) > 2):
            print('state 0')
            petStateLastSwitch = time()
            petState = 0
        if (round(petY) >= screenSize.height - 100):
            petVelY = -300
            petVelX = -300
            petState = 4
            petY = screenSize.height - 101
    window.after(1,update)

window = tk.Tk()

img = Image.open('pet.png').resize((100,100))
frame = ImageTk.PhotoImage(img)

window.overrideredirect(True)
window.wm_attributes('-transparentcolor','black')

window.attributes('-topmost', True)
label = tk.Label(window,image=frame,bd=0,bg='black')
label.pack()

def OnMouseDown(event):
    global petDragging
    petDragging = True

def OnMouseUp(event):
    global petDragging
    petDragging = False

window.bind("<ButtonPress-1>",OnMouseDown)
window.bind('<ButtonRelease-1>',OnMouseUp)
window.after(1,update)

window.mainloop()

