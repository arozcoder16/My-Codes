import pygame as pg

pg.init()
screen = pg.display.set_mode((700,200))

red = (255,0,0)
yellow = (255,255,0)
purple = (106,90,205)
white = (255,250,240)
black = (0,0,0)

screen.fill(purple)
pg.draw.ellipse(screen,yellow,(375,110,50,25))
pg.draw.ellipse(screen,black,(375,110,50,25),5)
pg.draw.ellipse(screen,red,(250,75,150,100))
pg.draw.ellipse(screen,black,(250,75,150,100),5)
pg.draw.ellipse(screen,black,(283,120,75,35),5)
pg.draw.ellipse(screen,white,(350,90,25,25))
pg.draw.ellipse(screen,black,(350,90,25,25),5)
pg.draw.ellipse(screen,black,(360,95,15,15))
pg.draw.line(screen,black,(230,95),(253,115),5)
pg.draw.line(screen,black,(225,105),(253,115),5)
pg.draw.line(screen,black,(220,115),(253,115),5)
pg.display.flip()
