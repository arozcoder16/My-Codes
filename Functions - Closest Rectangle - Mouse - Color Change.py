import pygame as pg
from math import sqrt

pg.init()
screen = pg.display.set_mode((800,800))

green = (0,255,0)
black = (0,0,0)
white = (255,255,255)

rect1 = pg.Rect(200,400,100,100)
rect2 = pg.Rect(600,400,100,100)
    
def closest_rect(rect1,rect2):
    mx,my = pg.mouse.get_pos()
    cx1,cy1 = rect1.center
    distance1 = sqrt((mx-cx1)**2 + (my-cy1)**2)

    cx2,cy2 = rect2.center
    distance2 = sqrt((mx-cx2)**2 + (my-cy2)**2)

    if distance1 > distance2:
        return rect2
    else:
        return rect1

while True:
    pg.event.pump()
    rectangles = closest_rect(rect1,rect2)
    screen.fill(white)

    pg.draw.rect(screen,black,rect1)
    pg.draw.rect(screen,black,rect2)
    pg.draw.rect(screen,green,rectangles)
    pg.display.flip()
