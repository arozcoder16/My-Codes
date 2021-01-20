import pygame as pg

pg.init()
screen = pg.display.set_mode((800,800))

black = (0,0,0)
white = (255,255,255)

clock = pg.time.Clock()
count = 0
font = pg.font.Font('freesansbold.ttf', 32)

while True:
    pg.event.pump()
    screen.fill(white)
    keys = pg.key.get_pressed()
    
    if keys[pg.K_UP]:
        count+=1

    if keys[pg.K_DOWN]:
        count-=1

    text = font.render(str(count), True, black)
    textRect = text.get_rect()
    textRect.center = (400,300)
    screen.blit(text,textRect)

    pg.display.flip()
    clock.tick(10)
