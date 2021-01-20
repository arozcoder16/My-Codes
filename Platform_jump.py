import pygame as pg
from sys import path
from sys import exit
from math import sqrt
import os

# Make path point to current directory
my_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(my_path)
path.append(my_path)

#Setup
pg.init()
screen = pg.display.set_mode((800,600)) #set your window size, (x,y)
pg.display.set_caption("Game Title")
clock = pg.time.Clock()

#colors
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)

class Samus():
    def __init__(self):
        self.hitbox = pg.Rect(100,100,30,30)
        self.speed_x = 0
        self.speed_y = 0
        self.gravity = 1
        self.jumping = 0

    def update(self):
        self.gravity += 1
        self.hitbox[1] += self.gravity
        self.hitbox[0] += self.speed_x

    def draw(self):
        pg.draw.rect(screen, black, self.hitbox)

s1 = Samus()
platform = pg.Rect(300,400,300,30)
platform2 = pg.Rect(200,500,400,30)
leftPress = 0

while True:

    # Input
    pg.event.pump()
    keys = pg.key.get_pressed()

    # Update
    s1.update()

    # Events
    if keys[pg.K_RIGHT]:
        s1.speed_x = 5
        if leftPress:
            leftPress = 0

    if keys[pg.K_LEFT] and leftPress == 0:
        leftPress = 1
        s1.speed_x = -5

    if keys[pg.K_UP] :#and s1.jumping == 0:
        s1.jumping = 1
        s1.speed_y = -15
        s1.hitbox[1] += s1.speed_y

    if s1.hitbox[1] >= 570:
        s1.gravity = 0
        s1.jumping = 0
        s1.speed_y = 0
        s1.hitbox[1] = 570
        if keys[pg.K_UP]:
            s1.hitbox[1] += s1.speed_y


    if s1.hitbox[1] >= (platform[1] - s1.hitbox[3]) and s1.hitbox.colliderect(platform):
        s1.gravity = 0
        s1.hitbox[1] = (platform[1] - s1.hitbox[3])
        if keys[pg.K_UP]:
            s1.hitbox[1] += s1.speed_y

    if s1.hitbox[1] >= (platform2[1] - s1.hitbox[3]) and s1.hitbox.colliderect(platform2):
        s1.gravity = 0
        s1.hitbox[1] = (platform2[1] - s1.hitbox[3])
        if keys[pg.K_UP]:
            s1.hitbox[1] += s1.speed_y

    # Drawings
    screen.fill(white)
    pg.draw.rect(screen, green, platform)
    pg.draw.rect(screen, green, platform2)
    s1.draw()
    pg.display.flip()

    # Clock
    clock.tick(20)
