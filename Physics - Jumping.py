import pygame as pg
import random

pg.init()
screen = pg.display.set_mode((800,600))
clock = pg.time.Clock()


white = (255,255,255)
red = (255,0,0)
line = pg.Rect(0,550,800,5)

class Ball():
    gravity = 1

    def __init__(self):
        self.hitbox = pg.Rect(300,550,50,50)
        self.speed_y = 0
        self.jumping = 0

    def update(self):
        self.hitbox[1] += self.speed_y
        self.speed_y += Ball.gravity

    def draw(self):
        pg.draw.ellipse(screen, red, self.hitbox)


ball = Ball()

while True:
    pg.event.pump()
    ball.update()

    keys = pg.key.get_pressed()

    if ball.hitbox[1] >= 550:
        ball.hitbox[1] = 550
        ball.speed_y = 0
        ball.jumping = 0

    if keys[pg.K_SPACE] == 1 and ball.jumping == 0:
        ball.jumping = 1
        ball.speed_y = -20

    screen.fill(white)
    ball.draw()
    pg.draw.rect(screen,red,line)
    pg.display.flip()

    clock.tick(30)
