import pygame as pg
import random as r

pg.init()
screen = pg.display.set_mode((800,800))
clock = pg.time.Clock()

white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
black = (0,0,0)

speed_x = 10
speed_y = 10

flappy_bird = pg.Rect(250,75,150,100)

pipe_upper_1 = pg.Rect(750,0,100,225)
pipe_upper_2 = pg.Rect(725,225,150,25)
pipe_lower_1 = pg.Rect(750,500,100,300)
pipe_lower_2 = pg.Rect(725,475,150,25)

score = 0

font = pg.font.Font('freesansbold.ttf', 32)
bird = pg.image.load("f_bird.png")
F_bird = pg.transform.scale(bird,(140,90))

gap = 225
state = 0

def start_menu():
    global state
    global font
    
    button_A = pg.Rect(375,450,100,100)
    
    text1 = font.render('Flappy Bird', True, black)
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
    
def game():
    global state,score,font,gap,speed_x,speed_y,pipe_upper_1,pipe_upper_2,pipe_lower_1,pipe_lower_2,flappy_bird
    
    while state == 1:
        pg.event.pump()
        L,M,R = pg.mouse.get_pressed()

        text = font.render(f'Score: {score}', True, black)
        textRect = text.get_rect()
        textRect.center = (150,50)

        pipe_upper_1[0] -= speed_x
        pipe_upper_2[0] -= speed_x
        pipe_lower_1[0] -= speed_x
        pipe_lower_2[0] -= speed_x
        flappy_bird[1] += speed_y

        if L == 1:
            flappy_bird[1] -= 20

        if pipe_upper_1[0] <=0:
            pipe_upper_1[0] = 800
            pipe_upper_2[0] = 775
            pipe_lower_1[0] = 800
            pipe_lower_2[0] = 775
            score += 1
            
            pipe_upper_1[3] = r.randint(0,575)
            pipe_upper_2[1] = pipe_upper_1[3]
            pipe_lower_2[1] = pipe_upper_1[3] + pipe_upper_2[3] + gap
            pipe_lower_1[1] = pipe_upper_1[3] + pipe_upper_2[3] + pipe_lower_2[3] + gap
            pipe_lower_1[3] = 800 - pipe_upper_1[3] - pipe_upper_2[3] - gap - pipe_lower_2[3]

        if pipe_upper_1[0] and pipe_lower_1[0] and pipe_upper_2[0] and pipe_lower_2[0] <= 0:
            speed_x = 10

        if pipe_upper_1.colliderect(flappy_bird) or pipe_lower_1.colliderect(flappy_bird) or pipe_upper_2.colliderect(flappy_bird) or pipe_lower_2.colliderect(flappy_bird):
            state = 2
            score = 0
            
            flappy_bird = pg.Rect(250,75,150,100)
            pipe_upper_1 = pg.Rect(750,0,100,225)
            pipe_upper_2 = pg.Rect(725,225,150,25)
            pipe_lower_1 = pg.Rect(750,500,100,300)
            pipe_lower_2 = pg.Rect(725,475,150,25)
            
        if pipe_upper_1[0] <= 0:
            pipe_upper_1[0] = 800
            pipe_upper_2[0] = 775
            pipe_lower_1[0] = 800
            pipe_lower_2[0] = 775
            score += 1

        screen.fill(white)
        screen.blit(F_bird,(flappy_bird[0],flappy_bird[1]))
        pg.draw.rect(screen,green,(pipe_upper_1))
        pg.draw.rect(screen,black,(pipe_upper_1),5)
        pg.draw.rect(screen,green,(pipe_upper_2))
        pg.draw.rect(screen,black,(pipe_upper_2),5)
        pg.draw.rect(screen,green,(pipe_lower_1))
        pg.draw.rect(screen,black,(pipe_lower_1),5)
        pg.draw.rect(screen,green,(pipe_lower_2))
        pg.draw.rect(screen,black,(pipe_lower_2),5)
        screen.blit(text,textRect)
        
        pg.display.flip()
        clock.tick(45)

def game_over_menu():
    global state
    global font
    
    button_B = pg.Rect(400,450,100,100)
    
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

        if L == 1 and button_B.collidepoint(Mx,My):
            state = 1

        screen.fill(white)
        pg.draw.rect(screen,green,button_B)
        screen.blit(text3,textRect3)
        screen.blit(text4,textRect4)
        screen.blit(text5,textRect5)
        pg.display.flip()

while True:
    if state == 0:
        start_menu()

    if state == 1:
        game()

    if state == 2:
        game_over_menu()
