import pygame as pg

pg.init()
screen = pg.display.set_mode((210,210))
clock = pg.time.Clock()

black = (0,0,0)
white = (255,255,255)

def dice(num):
    pg.draw.rect(screen,black,(0,0,210,210),5)
    pg.event.pump()
    
    if num == 1:
        pg.draw.ellipse(screen,black,(80,80,50,50))

    if num == 2:
        pg.draw.ellipse(screen,black,(10,10,50,50))
        pg.draw.ellipse(screen,black,(150,150,50,50))

    if num == 3:
        pg.draw.ellipse(screen,black,(10,10,50,50))
        pg.draw.ellipse(screen,black,(80,80,50,50))
        pg.draw.ellipse(screen,black,(150,150,50,50))

    if num == 4:
        pg.draw.ellipse(screen,black,(10,10,50,50))
        pg.draw.ellipse(screen,black,(10,150,50,50))
        pg.draw.ellipse(screen,black,(150,10,50,50))
        pg.draw.ellipse(screen,black,(150,150,50,50))

    if num == 5:
        pg.draw.ellipse(screen,black,(10,10,50,50))
        pg.draw.ellipse(screen,black,(10,150,50,50))
        pg.draw.ellipse(screen,black,(80,80,50,50))
        pg.draw.ellipse(screen,black,(150,10,50,50))
        pg.draw.ellipse(screen,black,(150,150,50,50))

    if num == 6:
        pg.draw.ellipse(screen,black,(10,10,50,50))
        pg.draw.ellipse(screen,black,(10,80,50,50))
        pg.draw.ellipse(screen,black,(10,150,50,50))
        pg.draw.ellipse(screen,black,(150,10,50,50))
        pg.draw.ellipse(screen,black,(150,80,50,50))
        pg.draw.ellipse(screen,black,(150,150,50,50))

screen.fill(white)
dice(6)
pg.display.flip()
clock.tick(1)
