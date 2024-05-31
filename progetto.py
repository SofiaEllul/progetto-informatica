import pygame, sys
from random import randint
from pygame.locals import *
from classe_nuvole import nuvolette
from classe_moneta import monetine
from classe_punti import Punteggio
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

home=pygame.image.load('immagini/menu.png')
icona=pygame.image.load('immagini/play.png')
icona_tom=pygame.image.load("immagini/FAST_TOM.png")

# (lavorando sul punteggio)

FPS=60
vel=10
vel_nuvole=10

WINDOW_SIZE= (605,500)
SCREEN= pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Talking Tom!")     

def immagini():
    global cielo, nuvole, moneta, cornice2, cornicegiu_x, cornicesu, cornicesu_x, tom, tom_x, tom_y
    SCREEN.blit(cielo, (0,0))
    for nuvola in nuvole:
        nuvola.movimento()
    for coin in moneta:
        coin.movimento()
    SCREEN.blit(cornice2, (cornicegiu_x, 437))
    SCREEN.blit(cornicesu, (cornicesu_x, 0))
    SCREEN.blit(tom, (tom_x, tom_y))

punti_y = 60
punti = Punteggio(SCREEN, [0,0], [605, punti_y])

def inizializza():
    global tom_x, tom_y, fast_tom
    global cornicesu_x, cornicegiu_x
    global nuvole, moneta, punti
    global home, icona
    cornicegiu_x=0
    cornicesu_x=-2
    tom_x, tom_y= 50, 150
    fast_tom=0
    nuvole=[]
    nuvole.append(nuvolette())
    moneta=[]
    moneta.append(monetine())
    
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
                punti.punti=0

            if event.type==pygame.QUIT:
                pygame.quit()
        aggiorna()

inizializza()

punti=Punteggio(SCREEN, (10,10), (30, 50))

inizio=True

while True: 

    if inizio:
        SCREEN.blit(home, (0,0))
        SCREEN.blit(icona, (125, 370))
        SCREEN.blit(icona_tom, (190, 220))
        icona_rect=icona.get_rect(topleft=(125, 370))
        aggiorna()
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                if icona_rect.collidepoint(pos):
                    print('x')
                    inizio=False
                    
    else:

        immagini()
        cornicegiu_x-=vel
        if cornicegiu_x<-300:
            cornicegiu_x=0

        cornicesu_x-=vel
        if cornicesu_x<-300:
            cornicesu_x=0

        fast_tom+=1
        tom_y+=fast_tom
        
        for event in pygame.event.get():
            if event.type==KEYDOWN and event.key==K_UP:
                fast_tom=-11
            if event.type==QUIT:
                pygame.quit()
                

        if nuvole[-1].rect.x < 150:
            nuvole.append(nuvolette())
            moneta.append(monetine())
            while moneta[-1].rect.top<nuvole[-1].rect.bottom and moneta[-1].rect.top>nuvole[-1].rect.top:
                moneta.pop()
                moneta.append(monetine())
        
        for nuvola in nuvole:
            tom_rect=pygame.transform.rotozoom(tom, 0, 0.8).get_rect(topleft=(tom_x, tom_y))
            if nuvola.rect.colliderect(tom_rect):
                gameover()

            if nuvola.rect.right<0:
                nuvole.remove(nuvola)
        immagini()
        
        
        for nuvola in nuvole:
            for coin in moneta:
                if nuvola.rect.colliderect(coin.rect):
                    moneta.remove(coin)

        for coin in moneta:
            if tom_rect.colliderect(coin.rect):
                print('x')
                punti.punti+=1
                moneta.remove(coin)
        punti.disegna()

        if tom_y<20 or tom_y>440:
            gameover()

        
     

    aggiorna()
