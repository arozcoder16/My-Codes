import pygame as pg
import random

pg.init()
screen = pg.display.set_mode((800,600))
clock = pg.time.Clock()


white = (255,255,255)
red = (255,0,0)

class Ball():
    gravity = 1

    def __init__(self):
        self.hitbox = pg.Rect(400,200,50,50)
        self.speed_y = 0
        self.jumping = 0

    def update(self):
        self.hitbox[1] += self.speed_y
        self.speed_y += Ball.gravity
        
    

    def draw(self):
        pg.draw.ellipse(screen, red, self.hitbox)


ball = Ball()
ball.speed_y = -20

while True:
    pg.event.pump()
    keys = pg.key.get_pressed()

    if keys[pg.K_UP] and leftPress == 0:
        leftPress
    
    ball.update()
    screen.fill(white)
    ball.draw()
    
    pg.display.flip()
    clock.tick(30)
