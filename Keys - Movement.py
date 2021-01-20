import pygame as pg

pg.init()
screen = pg.display.set_mode((800,800))

blue = (0,0,255)
white = (255,255,255)

square = pg.Rect(400,400,50,50)
clock = pg.time.Clock()

while True:
    pg.event.pump()
    screen.fill(white)
    keys = pg.key.get_pressed()

    if square[1] > 0:
        if keys[pg.K_UP]:
            square[1]-=5

    if square[1] < 750:
        if keys[pg.K_DOWN]:
            square[1]+=5
            
    if square[0] > 0:
        if keys[pg.K_LEFT]:
            square[0]-=5
            
    if square[0] <750:
        if keys[pg.K_RIGHT]:
            square[0]+=5

    pg.draw.rect(screen,blue,square)
    pg.display.flip()
    clock.tick(100)
