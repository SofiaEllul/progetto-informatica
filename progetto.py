import pygame, sys
from random import randint
from pygame.locals import *

pygame.init()
Clock= pygame.time.Clock()

cielo= pygame.image.load("immagini/cielo.png")
cornice2= pygame.image.load("immagini/cornice2.png")
cornicesu= pygame.transform.flip(cornice2, False, True)
nuvoletta= pygame.image.load("immagini/nuvoletta.png")
tom= pygame.image.load("immagini/tom .png")

FPS=50
vel=3
vel_nuvole=3

WINDOW_SIZE= (605,500)
SCREEN= pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Talking Tom!")

class nuvolette:
    def __init__(self):
        self.x=100
        self.y=randint(-75,150)
    def movimento(self):
        self.x=vel
        SCREEN.blit(nuvoletta, (self.x,self.y+randint(0,99)))

def immagini():
    SCREEN.blit(cielo, (0,0))
    for nuvola in nuvole:
        nuvola.movimento()
    SCREEN.blit(cornice2, (cornicegiu_x, 348))
    SCREEN.blit(cornicesu, (cornicesu_x, 0))
    SCREEN.blit(tom, (tom_x, tom_y))

def inizializza():
    global tom_x, tom_y, fast_tom
    global cornicesu_x, cornicegiu_x
    global nuvole
    cornicegiu_x=0
    cornicesu_x=-2
    tom_x, tom_y= -100, 150
    fast_tom=0
    nuvole=[]
    nuvole.append(nuvolette())

def aggiorna():
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

inizializza()

while True:
    cornicegiu_x-=vel
    if cornicegiu_x<-608:
        cornicegiu_x=0

    cornicesu_x-=vel
    if cornicesu_x<-608:
        cornicesu_x=0

    fast_tom+=1
    tom_y+=fast_tom

    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN and event.key==pygame.K_UP:
            fast_tom=-10
        if event.type==QUIT:
            pygame.quit()

    immagini()
    aggiorna()
