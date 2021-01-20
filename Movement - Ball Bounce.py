import pygame as pg

pg.init()
screen = pg.display.set_mode((800,800))
clock = pg.time.Clock()

white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
speed_x = 10
speed_y = 10

ball = pg.Rect(0,250,50,50)

while True:
    ball[0] += speed_x
    ball[1] += speed_y

    if ball[0] <= 0:
        speed_x = 10
        
    if ball[0] >= 750:
        speed_x = -10

    if ball[1] <= 0:
        speed_y =10
        
    if ball[1] >= 750:
        speed_y = -10

    screen.fill(white)
    pg.draw.ellipse(screen,red,(ball))
    pg.display.flip()
    clock.tick(45)
