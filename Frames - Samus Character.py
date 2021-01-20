import pygame as pg
import random as r

pg.init()
screen = pg.display.set_mode((800,800))
clock = pg.time.Clock()

black = (0,0,0)
white = (255,255,255)

class Samus():
    def __init__(self,x,y):
        self.hitbox = pg.Rect(x,y,50,100)
        self.speed_x = 10

        self.walk = []
        
        self.walk.append(pg.image.load('right_0.png'))
        self.walk.append(pg.image.load('right_1.png'))
        self.walk.append(pg.image.load('right_2.png'))
        self.walk.append(pg.image.load('right_3.png'))
        self.walk.append(pg.image.load('right_4.png'))  
        self.walk.append(pg.image.load('right_5.png'))
        self.walk.append(pg.image.load('right_6.png'))

        self.frame = 0
                         
    def update(self):
        self.hitbox[0] += self.speed_x

        if self.speed_x != 0:
            self.frame += 1

        if self.frame > 6:
            self.frame = 0

    def draw(self):
        screen.blit(self.walk[self.frame],(self.hitbox[0],self.hitbox[1]))

S = Samus(0,100)

while True:
    S.update()
    screen.fill(white)
    S.draw()
    pg.display.flip()
    clock.tick(10)
