import pygame as pg

pg.init()
screen = pg.display.set_mode((800,800))

green = (0,255,0)
brown = (139,69,19)
white = (255,250,240)

cookie_color = brown
cookie = pg.Rect(100,100,500,500)

while True:
    pg.event.pump()
    mx,my = pg.mouse.get_pos()
    L,M,R = pg.mouse.get_pressed()

    if cookie.collidepoint(mx,my) and L == 1:
        cookie_color = green

    else:
        cookie_color = brown

    screen.fill(white)
    pg.draw.ellipse(screen,cookie_color,cookie)    
    pg.display.flip()
