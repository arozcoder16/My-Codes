import pygame as pg

pg.init()
screen = pg.display.set_mode((800,800))
clock = pg.time.Clock()

yellow = (255,255,0)
black = (0,0,0)
white = (255,255,255)
purple = (255,0,255)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
    
class Ball():
    w = 50
    h = 50

    def __init__(self,paint,x,y):
        self.colour = paint
        self.hitbox = pg.Rect(x,y,Ball.w,Ball.h)
        self.speed_x = 10
        self.speed_y = 10
    
    def update(self):
        self.hitbox[0] += self.speed_x
        self.hitbox[1] += self.speed_y

        if self.hitbox[0] <= 0:
            self.speed_x = 10
            
        if self.hitbox[0] >= 750:
            self.speed_x = -10

        if self.hitbox[1] <= 0:
            self.speed_y = 10
            
        if self.hitbox[1] >= 750:
            self.speed_y = -10
            
    def draw(self):
        pg.draw.ellipse(screen,self.colour,self.hitbox)

b1 = Ball(yellow,0,150)
b2 = Ball(red,0,250)
b3 = Ball(blue,0,350)
b4 = Ball(green,0,450)
b5 = Ball(purple,0,550)
b6 = Ball(black,0,650)

while True:
    b1.update(),b2.update(),b3.update(),b4.update(),b5.update(),b6.update()
    screen.fill(white)
    b1.draw(),b2.draw(),b3.draw(),b4.draw(),b5.draw(),b6.draw()
    pg.display.flip()
    clock.tick(45)
