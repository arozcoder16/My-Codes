import pygame as pg

pg.init()
screen = pg.display.set_mode((800,600))

red = (255,0,0)
pg.draw.rect(screen,red,(250,75,100,50),5)
pg.display.flip()
