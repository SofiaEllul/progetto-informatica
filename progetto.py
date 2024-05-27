import pygame, sys
from random import randint
from pygame.locals import *
rect=pygame.rect

pygame.init()
Clock= pygame.time.Clock()

cielo= pygame.image.load("immagini/cielo.png")
cornice2= pygame.image.load("immagini/cornice2.png")
cornicesu= pygame.transform.flip(cornice2, False, True)
nuvoletta= pygame.image.load("immagini/nuvoletta.png")
tom= pygame.image.load("immagini/tom .png")
game_over=pygame.image.load("immagini/gameover.png")
monetina=pygame.image.load('immagini/monetina.png')

FPS=50
vel=12
vel_nuvole=12


WINDOW_SIZE= (605,500)
SCREEN= pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Talking Tom!")

class monetine:
    def __init__(self):
        self.x=400
        self.y=randint(-10,150)
    def movimento(self):
        self.x-=vel
        SCREEN.blit(monetina, (self.x,self.y+100))

class nuvolette:
    def __init__(self):
        self.x=600
        self.y=randint(-20,150)
    def movimento(self):
        self.x-=vel
        SCREEN.blit(nuvoletta, (self.x,self.y+100))

def immagini():
    SCREEN.blit(cielo, (0,0))
    for nuvola in nuvole:
        nuvola.movimento()
    SCREEN.blit(cornice2, (cornicegiu_x, 245))
    SCREEN.blit(cornicesu, (cornicesu_x, 0))
    SCREEN.blit(tom, (tom_x, tom_y))

def inizializza():
    global tom_x, tom_y, fast_tom
    global cornicesu_x, cornicegiu_x
    global nuvole, moneta
    cornicegiu_x=0
    cornicesu_x=-2
    tom_x, tom_y= -100, 150
    fast_tom=0
    nuvole=[]
    nuvole.append(nuvolette())
    moneta=[]
    moneta.append(monetine())
    
tom=rect
nuvola=rect

def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

def gameover():
    SCREEN.blit(game_over, (190,118))
    aggiorna()
    ricomincia=False
    while not ricomincia:
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                inizializza()
                ricomincia=True
            if event.type==pygame.QUIT:
                pygame.quit()

inizializza()

while True:
    cornicegiu_x-=vel
    if cornicegiu_x<-300:
        cornicegiu_x=0

    cornicesu_x-=vel
    if cornicesu_x<-300:
        cornicesu_x=0

    fast_tom+=1
    tom_y+=fast_tom

    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN and event.key==pygame.K_UP:
            fast_tom=-10
        if event.type==QUIT:
            pygame.quit()
    
    if nuvole[-1].x < 150:
        nuvole.append(nuvolette())

    if moneta[-1].x < 150:
        moneta.append(monetine())
    
    for nuvola in nuvole:
        if nuvola.rect.collide_rect(tom.get_rect()):
            gameover()

    if tom_y<-20 or tom_y>370:
        gameover()

    immagini()
    aggiorna()
