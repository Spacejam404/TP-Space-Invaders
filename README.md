# TP-Space-Invaders
prototype to update

Space invaders on µpython on STM32F407 by STmicroelectronics
I've done what i could in the given time (that was 2 days ago (today is 25/05/21) but had some issues implementing bullets,
The starship moves and fires and bullets erase everything in their path.
You can fire a maximum of 15 bullets at the same time (can be changed in the code)
be careful if you change the delays between each movement as it adds to other delays (move starship then all bullets then repeat) so the more delay you add, the slower you sapceship moves while bullets are on the screen (may optimize it later)
Still need to add a game end and makes aliens fire and move

Altough it was a fun project

Note:

Flash the code on your cartd then connect it via µUSB and UART to play on a screen
Once flashed, eject the PYBFLASH properly then push the Reset(black) button
(You'll need Putty/Teraterm/others to play on screen) (baudrate = 115200)

Hope you'll like it and don't be shy to add things if you want as long as the code still works!


Controls:

Move by rolling the card left or right
Fire by pressing the blue button ( you can do auto fire by continuously pushing till you have max bullets on screen)
