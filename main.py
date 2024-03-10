import pyautogui
import random
import tkinter as tk
from PIL import Image, ImageTk
from time import time
import math
from pygame import mixer
from pygame.mixer import Sound
import json

config = json.load(open('config.json'))

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

petFriction = True

sounds = {}
currentSound = None
currentSoundGroup = None
currentSoundStart = 0
currentSprite = 'pet.png'

def changeSprite(path):
    global currentSprite
    currentSprite = path
    img = Image.open(path).resize((100,100))
    frame = ImageTk.PhotoImage(img)
    label.config(image=frame)
    label.image = frame

def justifySprite(path):
    path = 'assets/sprites/' + path
    global currentSprite
    if (currentSprite != path):
        changeSprite(path)

def playSound(name):
    global currentSound
    global currentSoundStart
    global currentSoundGroup
    if (name in config['allowed_sounds'].keys()):
        if (not config['allowed_sounds'][name]):
            print('Attempted to play disabled sound: {}'.format(name))
            return
    if (name in sounds.keys()):
        if (not currentSound or not currentSoundGroup):
            ID = random.randint(0,(len(sounds[name]['sounds']) - 1))
            sounds[name]['sounds'][ID].play()
            currentSoundGroup = sounds[name]
            currentSound = sounds[name]['sounds'][ID]
            currentSoundStart = time()
        else:
            if (currentSoundGroup['priority'] <= sounds[name]['priority']):
                currentSound.stop()
                ID = random.randint(0,(len(sounds[name]['sounds']) - 1))
                sounds[name]['sounds'][ID].play()
                currentSoundGroup = sounds[name]
                currentSound = sounds[name]['sounds'][ID]
                currentSoundStart = time()

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
    global currentSound
    global currentSoundStart
    global currentSoundGroup
    global petFriction
    delta = time() - lastTick
    lastTick = time()
    mouseX,mouseY = window.winfo_pointerxy()
    window.geometry('100x100+{}+{}'.format(round(petX),round(petY)))
    if (currentSound and currentSoundGroup):
        if (currentSoundStart + currentSound.get_length() <= time()):
            currentSound = None
            currentSoundGroup = None
    if (not petDragging):
        if (petY < screenSize.height - 100):
            petVelY += delta * 1000
        else:
            petVelY = abs(petVelY) * -0.2
            petY = screenSize.height - 100
        
        if (petFriction):
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
    if (str(petState) in config['allowed_states']):
        if (not config['allowed_states'][str(petState)]):
            print('Kicked out of disabled state: state {}'.format(petState))
            petState = 0
    if (petState == 0):
        justifySprite('pet.png')
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
        elif (random.random() <= 0.001 and (time() - petStateLastSwitch) > 3):
            print('state 6')
            petState = 6
            petStateLastSwitch = time()
            playSound('drink')
        elif (random.random() <= 0.001 and (time() - petStateLastSwitch) > 3):
            print('state 7')
            petState = 7
            petStateLastSwitch = time()
        elif (random.random() <= 0.001 and (time() - petStateLastSwitch) > 3 and (round(petY) == (screenSize.height - 100))):
            print('state 9')
            petY = screenSize.height - 101
            petVelY = -100
            petState = 9
            petStateLastSwitch = time()
        elif (random.random() <= 0.001 and (time() - petStateLastSwitch) > 3):
            if ((petX + 50) > screenSize.width//2):
                print('state 11')
                petState = 11
                petStateLastSwitch = time()
                playSound('speedrun')
            else:
                print('state 10')
                petState = 10
                petStateLastSwitch = time()
                playSound('speedrun')
            

    elif (petState == 1):
        justifySprite('pet.png')
        petX += 100 * delta
        if (random.random() <= 0.001 and (time() - petStateLastSwitch) > 3):
            print('state 0')
            petStateLastSwitch = time()
            petState = 0
        if (petX > screenSize.width - 100):
            petState = 2
            print('Turning around')
    elif (petState == 2):
        justifySprite('pet.png')
        petX -= 100 * delta
        if (random.random() <= 0.001 and (time() - petStateLastSwitch) > 3):
            print('state 0')
            petStateLastSwitch = time()
            petState = 0
        if (petX < 0):
            petState = 1
            print('Turning around')
    elif (petState == 3):
        justifySprite('pet.png')
        if (random.random() <= 0.001 and (time() - petStateLastSwitch) > 2):
            print('state 0')
            petStateLastSwitch = time()
            petState = 0
        if (round(petY) >= screenSize.height - 100):
            petVelY = -300
    elif (petState == 4):
        justifySprite('pet.png')
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
        justifySprite('pet.png')
        if (random.random() <= 0.001 and (time() - petStateLastSwitch) > 2):
            print('state 0')
            petStateLastSwitch = time()
            petState = 0
        if (round(petY) >= screenSize.height - 100):
            petVelY = -300
            petVelX = -300
            petState = 4
            petY = screenSize.height - 101
    elif (petState == 6):
        justifySprite('sprite.png')
        if (currentSoundGroup != sounds['drink']):
            print('Knocked out of state 6')
            petStateLastSwitch = time()
            petState = 0
    elif (petState == 7):
        justifySprite('pet.png')
        if (petX > screenSize.width // 10):
            petVelX = -300
        if (petX < screenSize.width // 10):
            petVelX = 300
        if (abs(petX - screenSize.width // 10) < 5):
            petState = 8
            print('state 8')
    elif (petState == 8):
        justifySprite('pet.png')
        petFriction = False
        if (petX < screenSize.width - 100):
            petVelX += 1000 * delta
        else:
            petVelX = -2000
            petVelY = -2000
            petState = 0
            print('state 0')
            petStateLastSwitch = time()
            petFriction = True
    elif (petState == 9):
        justifySprite('pet.png')
        if (petY >= screenSize.height - 100):
            petVelY *= -1.5
            petY = screenSize.height - 101
        if (petY <= 5):
            print('state 0')
            petState = 0
            petStateLastSwitch = time()
    elif (petState == 10):
        justifySprite('pet.png')
        if (petY >= screenSize.height - 100):
            petVelY = -200
            petVelX = 200
            petY = screenSize.height - 101
        if (petX >= screenSize.width - 110):
            if (currentSound and currentSoundGroup):
                if (currentSoundGroup == sounds['speedrun']):
                    currentSound.stop()
                    currentSound = None
                    currentSoundGroup = None
                    petState = 0
                    petStateLastSwitch = time()
                    print('state 0')
            else:
                petState = 0
                petStateLastSwitch = time()
                print('state 0')
        if (currentSoundGroup != sounds['speedrun'] and petState == 10):
            petState = 0
            petStateLastSwitch = time()
            print('state 0')
    elif (petState == 11):
        justifySprite('pet.png')
        if (petY >= screenSize.height - 100):
            petVelY = -200
            petVelX = -200
            petY = screenSize.height - 101
        if (petX <= 10):
            if (currentSound and currentSoundGroup):
                if (currentSoundGroup == sounds['speedrun']):
                    currentSound.stop()
                    currentSound = None
                    currentSoundGroup = None
                    petState = 0
                    petStateLastSwitch = time()
                    print('state 0')
            else:
                petState = 0
                petStateLastSwitch = time()
                print('state 0')
        if (currentSoundGroup != sounds['speedrun'] and petState == 10):
            petState = 0
            print('state 0')

    window.after(1,update)

window = tk.Tk()

img = Image.open('assets/sprites/pet.png').resize((100,100))
frame = ImageTk.PhotoImage(img)

window.overrideredirect(True)
window.wm_attributes('-transparentcolor','#010011')

window.attributes('-topmost', True)
label = tk.Label(window,image=frame,bd=0,bg='#010011')
label.pack()

def OnMouseDown(event):
    global petDragging
    global sounds
    petDragging = True
    playSound('pickup')

def OnMouseUp(event):
    global petDragging
    global petVelX
    global petVelY
    global sounds
    global currentSound
    global currentSoundGroup
    petDragging = False
    if (math.sqrt(petVelX**2 + petVelY**2) > 1000):
        playSound('launch')
    else:
        if (currentSound and currentSoundGroup):
            if (currentSoundGroup == sounds['pickup']):
                currentSound.stop()
                currentSound = None
                currentSoundGroup = None


window.bind("<ButtonPress-1>",OnMouseDown)
window.bind('<ButtonRelease-1>',OnMouseUp)
window.after(1,update)

def init():
    global pickupSound
    mixer.init()
    sounds['pickup'] = {'sounds': [Sound('assets/sounds/pickup1.mp3'),Sound('assets/sounds/pickup2.mp3')],'priority': 2}
    sounds['launch'] = {'sounds': [Sound('assets/sounds/launch1.mp3')],'priority': 3}
    sounds['drink'] = {'sounds': [Sound('assets/sounds/drink1.mp3')],'priority': 1}
    sounds['speedrun'] = {'sounds': [Sound('assets/sounds/speedrun1.mp3')],'priority': 1}


window.after(1,init)
window.mainloop()

