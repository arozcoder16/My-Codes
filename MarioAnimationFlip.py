import pygame as pg

from sys import path
from sys import exit
import os
import expy


my_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(my_path)
path.append(my_path)

#Setup

pg.init()
screen = pg.display.set_mode((800,600)) #set your window size, (x,y)
pg.display.set_caption("mario animation")
clock = pg.time.Clock()

class Mario():
    gravity = 1

    def __init__(self,x,y):
        self.hitbox = pg.Rect(x,y,50,100)
        self.speed_x = 10
        self.speed_y = 0
        self.jumping = 0
        self.frame = 0
        self.direction = 1
        self.stand = []
        self.walk_right = []
        self.walk_left = []
        self.walk_right.append(pg.image.load("A3.png"))
        self.walk_right.append(pg.image.load("A4.png"))
        self.walk_right.append(pg.image.load("A5.png"))
        self.stand.append(pg.image.load("A11.png"))  #left cape down --> standing & jumping up
        self.stand.append(pg.image.load("A12.png"))  #right cape down --> standing & jumping up
        self.stand.append(pg.image.load("A8.png"))   #left cape up --> falling down
        self.stand.append(pg.image.load("A15.png"))  #right cape up -->falling down

    def update(self):
        pg.event.pump()
        keys = pg.key.get_pressed()
        if keys[pg.K_RIGHT] == 1:
            self.speed_x = 10
            self.direction = 1
        elif keys[pg.K_LEFT] == 1:
            self.speed_x = -10
            self.direction = -1
        else:
            self.speed_x = 0
        self.hitbox[0] += self.speed_x
        if self.speed_x != 0:
            self.frame += 1
        if self.frame>2:
            self.frame = 0
        self.hitbox[1] += self.speed_y
        self.speed_y += Mario.gravity

    def draw(self):
        if self.speed_x > 0: #moving right
            screen.blit(self.walk_right[self.frame],(self.hitbox[0],self.hitbox[1]))
        elif self.speed_x < 0: #moving left
            screen.blit(self.walk_left[self.frame],(self.hitbox[0],self.hitbox[1]))
        elif self.hitbox[1] == 550 and self.direction == 1: #standing right
            screen.blit(self.stand[1],(self.hitbox[0],self.hitbox[1]))
        elif self.hitbox[1] == 550 and self.direction == -1: #standing left
            screen.blit(self.stand[0],(self.hitbox[0],self.hitbox[1]))
        elif self.speed_y > 0 and self.direction == 1: #falling down right
            screen.blit(self.stand[3],(self.hitbox[0],self.hitbox[1]))
        elif self.speed_y > 0 and self.direction == -1: #falling down left
            screen.blit(self.stand[2],(self.hitbox[0],self.hitbox[1]))
        elif self.speed_y < 0 and self.direction == 1: #jumping up right
            screen.blit(self.stand[1],(self.hitbox[0],self.hitbox[1]))
        elif self.speed_y < 0 and self.direction == -1: #jumping up left
            screen.blit(self.stand[0],(self.hitbox[0],self.hitbox[1]))

    def flip(self):
        for frame in self.walk_right:
            flipped_frame = pg.transform.flip(frame,True,False)
            self.walk_left.append(flipped_frame)

white = (255,255,255)
mario = Mario(200,350)
mario.flip()

while True:
    pg.event.pump()
    screen.fill(white)
    mario.update()
    mario.draw()
    keys = pg.key.get_pressed()
    if mario.hitbox[1] >= 550:
        mario.hitbox[1] = 550
        mario.speed_y = 0
        mario.jumping = 0
    if keys[pg.K_SPACE] == 1 and mario.jumping == 0:
        mario.jumping = 1
        mario.speed_y = -10
    pg.display.flip()
    clock.tick(20)
