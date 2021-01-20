import pygame as pg

pg.init()
screen = pg.display.set_mode((800,800))

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,250,240)

while True:
    pg.event.pump()
    L,M,R = pg.mouse.get_pressed()

    if L == 1:
        screen.fill(red)

    elif M == 1:
        screen.fill(green)

    elif R == 1:
        screen.fill(blue)

    else:
        screen.fill(white)

    pg.display.flip()
