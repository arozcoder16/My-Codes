import pygame as pg

pg.init()
screen = pg.display.set_mode((800,800))
clock = pg.time.Clock()

white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
yellow = (255,255,0)
purple = (106,90,205)
white = (255,250,240)
black = (0,0,0)

state = 0

def red1():
    global state
    button_A = pg.Rect(300,250,250,100)

    while state == 0:
        pg.event.pump()
        Mx,My = pg.mouse.get_pos()
        L,M,R = pg.mouse.get_pressed()

        if L == 1 and button_A.collidepoint(Mx,My):
            state = 1

        screen.fill(white)
        pg.draw.rect(screen,red,button_A)
        pg.display.flip()

def green1():
    global state
    button_B = pg.Rect(300,400,250,100)

    while state == 1:
        pg.event.pump()
        Mx,My = pg.mouse.get_pos()
        L,M,R = pg.mouse.get_pressed()

        if L == 1 and button_B.collidepoint(Mx,My):
            state = 0

        screen.fill(white)
        pg.draw.rect(screen,green,button_B)
        pg.display.flip()

while True:
    if state == 0:
        red1()

    if state == 1:
        green1()

