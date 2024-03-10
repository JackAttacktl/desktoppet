# Desktop pet
Starring **Goner Girl** (by retty7.)

# States
State 0: Idle


State 1: Moving right

State 2: Moving left


State 3: Jumping in place


State 4: Jumping up and right (Goes to state 5 when ground touched)

State 5: Jumping up and left (Goes to state 4 when ground touched)


State 6: Drinking McDonalds Sprite


State 7: Going to the left side of the screen (Goes to state 8 when reached)

State 8: Sliding to the right side of screen very fast (friction turned off, goes Idle when reaches the end of the screen)


State 9: Bouncing with each bounce launching Pet higher than the last one (Goes Idle when top of the screen is reached)


State 10: Speedrunning to the right side of the screen (with sound, Goes Idle when right side of the screen is reached or the sound ends)

State 11: Speedrunning to the left of the screen (with sound, Goes Idle when left side of the screen is reached or the sound ends)

# Sounds
All sounds can be found in /assets/sounds


State 6: Plays a Roblox Bloxy Cola drinking sound (drink1.mp3)

State 10 & 11: Plays a keyboard spamming sound (speedrun1.mp3)

Picking up: Plays Markiplier "No stop what are you doing" (pickup1.mp3) or Penguinz0 (MoistCr1TiKaL) screaming from a wasp (pickup2.mp3)

Flinging (launching): Plays Markiplier not getting over it (Markiplier raging from Getting Over It but it's datamoshed) (launch1.mp3)



# Sprites
All sprites can be found in /assets/sprites


States 0,1,2,3,4,5,7,8,9,10,11: pet.png

State 6: sprite.png


# Config (DEBUG ONLY)
## Allowed States
Change a state from "true" to "false" to disable it

Note: Some states will still play their respective sounds but not move. (States 10 & 11)

Note: Some states might still perform their beginning actions, such as jumping up a little bit (State 9, possibly States 7 & 8)



## Allowed Sounds
Change a sound from "true" to "false" to disable it

Note: Some states DEPEND on the sounds to function! Disabling the sound can also disable the State!

(State 6 depends on "drink", States 10 & 11 depend on "speedrun")



# Dragging
Pet can be picked up by clicking and dragging

If flung, they will scream at you (can be disabled in the allowed sounds menu)


# Closing
To close, simply click on Pet to focus on it, and Alt+F4

Alternitively, is pet has gone missing, just go to the task manager and search for the main.exe process

or type in Command Prompt (in the pet root directory) "taskkill /F /IM main.exe"

