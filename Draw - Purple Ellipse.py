import pygame as pg

pg.init()

screen = pg.display.set_mode((800,600))
purple = (255,0,255)

pg.draw.ellipse(screen,purple,(250,75,100,50))
pg.display.flip()
