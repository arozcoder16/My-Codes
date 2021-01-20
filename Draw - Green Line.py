import pygame as pg

pg.init()

screen = pg.display.set_mode((800,600))
green = (0,255,0)
pg.draw.line(screen,green,(75,55),(250,175),6)
pg.display.flip()
