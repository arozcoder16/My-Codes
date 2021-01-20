import pygame as pg

start_ticks = pg.time.get_ticks() 

pg.init()
screen = pg.display.set_mode((600,700))
clock = pg.time.Clock()

red = (255,0,0)
black = (0,0,0)
blue = (0,0,255)
white = (255,255,255)

square = pg.Rect(250,100,30,30)

Maze = []

#vertical
Maze.append(pg.Rect(34,125,6,510))
Maze.append(pg.Rect(540,125,6,510))
Maze.append(pg.Rect(85,325,6,105))
Maze.append(pg.Rect(235,329,6,103))
Maze.append(pg.Rect(85,530,6,55))
Maze.append(pg.Rect(390,532,6,105))
Maze.append(pg.Rect(389,175,6,55))
Maze.append(pg.Rect(185,535,6,55))
Maze.append(pg.Rect(135,579,6,55))
Maze.append(pg.Rect(337,582,6,55))
Maze.append(pg.Rect(237,480,6,153))
Maze.append(pg.Rect(340,225,6,110))
Maze.append(pg.Rect(439,225,6,210))
Maze.append(pg.Rect(235,225,6,57))
Maze.append(pg.Rect(185,175,6,155))
Maze.append(pg.Rect(135,175,6,55))
Maze.append(pg.Rect(285,175,6,55))
Maze.append(pg.Rect(490,175,6,55))
Maze.append(pg.Rect(490,275,6,55))
Maze.append(pg.Rect(287,277,6,208))
Maze.append(pg.Rect(490,380,6,206))
Maze.append(pg.Rect(337,430,6,100))
Maze.append(pg.Rect(185,430,6,55))
Maze.append(pg.Rect(388,430,6,55))
Maze.append(pg.Rect(440,480,6,55))
Maze.append(pg.Rect(285,530,6,57))
Maze.append(pg.Rect(237,125,6,57))


#horizontal
Maze.append(pg.Rect(35,125,207,6))
Maze.append(pg.Rect(287,125,258,6))
Maze.append(pg.Rect(34,631,260,6))
Maze.append(pg.Rect(340,631,206,6))
Maze.append(pg.Rect(85,175,55,6))
Maze.append(pg.Rect(288,175,55,6))
Maze.append(pg.Rect(437,175,55,6))
Maze.append(pg.Rect(35,225,55,6))
Maze.append(pg.Rect(135,225,260,6))
Maze.append(pg.Rect(85,277,105,6))
Maze.append(pg.Rect(85,377,107,6))
Maze.append(pg.Rect(85,428,155,6))
Maze.append(pg.Rect(340,277,105,6))
Maze.append(pg.Rect(340,430,55,6))
Maze.append(pg.Rect(439,225,55,6))
Maze.append(pg.Rect(439,378,55,6))
Maze.append(pg.Rect(439,580,55,6))
Maze.append(pg.Rect(490,327,55,6))
Maze.append(pg.Rect(388,327,55,6))
Maze.append(pg.Rect(388,480,55,6))
Maze.append(pg.Rect(288,530,55,6))
Maze.append(pg.Rect(288,580,55,6))
Maze.append(pg.Rect(35,580,55,6))
Maze.append(pg.Rect(35,480,105,6))
Maze.append(pg.Rect(135,530,105,6))
Maze.append(pg.Rect(237,277,55,6))
Maze.append(pg.Rect(135,328,105,6))
Maze.append(pg.Rect(290,377,105,6))

while True:
    pg.event.pump()
    keys = pg.key.get_pressed()
    screen.fill(white)
    
    for wall in Maze:
        pg.draw.rect(screen,black,wall)

    for wall in Maze:
        if square.colliderect(wall):
            square = pg.Rect(250,100,25,25)
            start_ticks = pg.time.get_ticks()
            
    if square[1] > 0:
        if keys[pg.K_UP]:
            square[1]-=5

    if square[1] < 675:
        if keys[pg.K_DOWN]:
            square[1]+=5
            
    if square[0] > 0:
        if keys[pg.K_LEFT]:
            square[0]-=5
            
    if square[0] < 575:
        if keys[pg.K_RIGHT]:
            square[0]+=5

    teleport1 = pg.draw.rect(screen,red,(147,490,30,30))
    teleport2 = pg.draw.rect(screen,red,(503,290,30,30))
    
    if square.colliderect(teleport1):
            square = pg.Rect(250,300,25,25)

    if square.colliderect(teleport2):
            square = pg.Rect(450,550,25,25)
        
    seconds =(pg.time.get_ticks()-start_ticks)/1000
    
    font = pg.font.Font('freesansbold.ttf', 32)
    text = font.render(f'Time: {seconds}', True, black)
    textRect = text.get_rect()
    textRect.center = (125,35)
    screen.blit(text,textRect)
 
    pg.draw.rect(screen,blue,square)
    pg.display.flip()
    clock.tick(25)
    
