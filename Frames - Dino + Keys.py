import pygame as pg
import random as r

pg.init()
screen = pg.display.set_mode((800,800))
clock = pg.time.Clock()

black = (0,0,0)
white = (255,255,255)

class Dino():
    gravity = 1
    
    def __init__(self,x,y):
        self.hitbox = pg.Rect(x,y,50,350)
        
        self.speed_x = 10
        self.speed_y = 0
        self.jumping = 0
        
        self.walk = []
        
        self.walk.append(pg.image.load('0.png'))
        self.walk.append(pg.image.load('1.png'))
        self.walk.append(pg.image.load('2.png'))  
        self.walk.append(pg.image.load('3.png'))
        self.walk.append(pg.image.load('4.png'))
        self.walk.append(pg.image.load('5.png'))
        
        self.frame = 0

    def flip(self):
        for i in range(len(self.walk)):
            self.walk[i] = pg.transform.flip(self.walk[i],1,0)
            
    def update(self):
        self.hitbox[0] += self.speed_x

        if self.speed_x != 0:
            self.frame += 1

        if self.frame > 5:
            self.frame = 0

        self.hitbox[1] += self.speed_y
        self.speed_y += GC.gravity

    def draw(self):
        screen.blit(self.walk[self.frame],(self.hitbox[0],self.hitbox[1]))

GC = Dino(0,350)

left_button = 0

while True:
    pg.event.pump()
    keys = pg.key.get_pressed()

    if keys[pg.K_RIGHT]:
        GC.speed_x = 10

        if left_button == 1:
            GC.flip()
            left_button = 0
        
    if keys[pg.K_LEFT] and left_button == 0:
        left_button = 1
        GC.speed_x = -10
        GC.flip()

    if GC.hitbox[1] >= 350:
        GC.hitbox[1] = 350
        GC.speed_y = 0
        GC.jumping = 0

    if keys[pg.K_UP] and GC.jumping == 0:
        GC.jumping = 1
        GC.speed_y = -15

    if keys[pg.K_DOWN]:
        GC.speed_y = 15
    
    screen.fill(white)
    GC.update()
    GC.draw()
    pg.display.flip()
    clock.tick(20)

