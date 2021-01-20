import pygame as pg
import random as r

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

score = 0
state = 0

font = pg.font.Font('freesansbold.ttf', 32)

class Cash():
    w = 40
    h = 40
    
    def __init__(self,paint):
        self.image = pg.image.load('Money bag.jpg')
        self.image = pg.transform.scale(self.image,(70,70))
        self.colour = paint
        x = r.randint(0,750)
        y = r.randint(0,750)
        self.hitbox = pg.Rect(x,y,Cash.w,Cash.h)
        
    def update(self):
        x = r.randint(0,725)
        y = r.randint(0,725)
        self.hitbox = pg.Rect(x,y,Cash.w,Cash.h)
        
    def draw(self):
        x = self.hitbox[0]
        y = self.hitbox[1]
        screen.blit(self.image,(x,y))

class CC():
    def __init__(self,paint,x,y):
        self.image = pg.image.load('cab_pic.jpg')
        
        self.image_up = pg.transform.scale(self.image,(65,100))

        w,h = self.image_up.get_size()
        
        self.image_down = pg.transform.rotate(self.image_up,180)
        self.image_left = pg.transform.rotate(self.image_up,90)
        self.image_right = pg.transform.rotate(self.image_up,270)
        
        self.colour = paint
        self.hitbox = pg.Rect(x,y,w,h)
        self.speed_x = 0
        self.speed_y = 0
    
    def update(self):
        self.hitbox[0] += self.speed_x
        self.hitbox[1] += self.speed_y

        if keys[pg.K_UP]:
            self.speed_x = 0
            self.speed_y =- 10

        if keys[pg.K_DOWN]:

            self.speed_x = 0
            self.speed_y =+ 10
            
        if keys[pg.K_LEFT]:
            self.speed_x =- 10
            self.speed_y = 0

        if keys[pg.K_RIGHT]:
            self.speed_x =+ 10
            self.speed_y = 0

    def border(self):
        if self.hitbox[1] < 0 or self.hitbox[1] > 750 or self.hitbox[0] < 0 or self.hitbox[0] > 750:
            return(1)
        else:
            return(0)

    def draw(self):
        if self.speed_x > 0:
            self.hitbox[2],self.hitbox[3] = self.image_right.get_size()
            screen.blit(self.image_right,(self.hitbox[0],self.hitbox[1]))
            
        if self.speed_x < 0:
            self.hitbox[2],self.hitbox[3] = self.image_left.get_size()
            screen.blit(self.image_left,(self.hitbox[0],self.hitbox[1]))
            
        if self.speed_y > 0:
            self.hitbox[2],self.hitbox[3] = self.image_down.get_size()
            screen.blit(self.image_down,(self.hitbox[0],self.hitbox[1]))
            
        if self.speed_y < 0:
            self.hitbox[2],self.hitbox[3] = self.image_up.get_size()
            screen.blit(self.image_up,(self.hitbox[0],self.hitbox[1]))

x = 400
y = 400
cab = CC(blue,x,y)
cash = Cash(red)

def game_over_menu():
    global state
    global font
    
    button = pg.Rect(400,450,100,100)
    
    text3 = font.render('Game Over', True, black)
    textRect3 = text3.get_rect()
    textRect3.center = (400,300)

    text4 = font.render('Try Again', True, black)
    textRect4 = text4.get_rect()
    textRect4.center = (400,350)

    text5 = font.render('Click on green box to restart Game', True, black)
    textRect5 = text5.get_rect()
    textRect5.center = (400,400)

    while state == 2:
        pg.event.pump()
        Mx,My = pg.mouse.get_pos()
        L,M,R = pg.mouse.get_pressed()

        if L == 1 and button.collidepoint(Mx,My):
            state = 1

        screen.fill(white)
        pg.draw.rect(screen,green,button)
        screen.blit(text3,textRect3)
        screen.blit(text4,textRect4)
        screen.blit(text5,textRect5)
        pg.display.flip()

def start_menu():
    global state
    global font
    
    button_A = pg.Rect(375,450,100,100)
    
    text1 = font.render('Cash Cab', True, black)
    textRect1 = text1.get_rect()
    textRect1.center = (400,300)

    text2 = font.render('Press Left Button on Red Box to start Game', True, black)
    textRect2 = text2.get_rect()
    textRect2.center = (400,350)
    
    while state == 0:
        pg.event.pump()
        Mx,My = pg.mouse.get_pos()
        L,M,R = pg.mouse.get_pressed()

        if L == 1 and button_A.collidepoint(Mx,My):
            state = 1

        screen.fill(white)
        pg.draw.rect(screen,red,button_A)
        screen.blit(text1,textRect1)
        screen.blit(text2,textRect2)
        pg.display.flip()

while True:
    if state == 0:
        start_menu()

    while state == 1:
        pg.event.pump()

        keys = pg.key.get_pressed()
        screen.fill(white)

        text = font.render(f'Score: {score}', True, black)
        textRect = text.get_rect()
        textRect.center = (100,50)
        screen.blit(text,textRect)

        if cab.hitbox.colliderect(cash.hitbox):
            cash.update()
            score+=1
            
        cab.update()
        cab.draw()

        if cab.border():
            state = 2
            game_over_menu()
            cab.hitbox[0] = x
            cab.hitbox[1] = y

        cash.draw()
        
        pg.display.flip()
        clock.tick(45)
