import pygame as pg

pg.init()

screen = pg.display.set_mode((800,600))

brown = (139,69,19)
white = (255,250,240)
black = (3,3,3)

pg.draw.rect(screen,brown,(100,100,200,400))
pg.draw.rect(screen,black,(150,150,100,80),5)
pg.draw.rect(screen,white,(150,150,100,80))
pg.draw.line(screen,black,(200,150),(200,230))
pg.draw.line(screen,black,(150,190),(250,190))
pg.draw.ellipse(screen,black,(120,310,25,25))
pg.display.flip()
