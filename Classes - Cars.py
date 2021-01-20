import pygame as pg

pg.init()
screen = pg.display.set_mode((800,800))
clock = pg.time.Clock()

yellow = (255,255,0)
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
    
class Car():
    w = 75
    h = 50

    def __init__(self,paint,x,y):
        self.colour = paint
        self.hitbox = pg.Rect(x,y,Car.w,Car.h)
        self.speed = 5

    def update(self):
        self.hitbox[0] += self.speed

    def draw(self):
        pg.draw.ellipse(screen,self.colour,self.hitbox)

car1 = Car(yellow,10,100)
car2 = Car(red,10,200)
car3 = Car(blue,10,300)

car1.speed = 20
car2.speed = 15
car3.speed = 10

while True:
    car1.update(),car2.update(),car3.update()
    screen.fill(white)
    car1.draw(),car2.draw(),car3.draw()
    pg.display.flip()
    clock.tick(30)
