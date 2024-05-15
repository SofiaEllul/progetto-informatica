import pygame, sys
from random import randint
from pygame.locals import *

pygame.init()
Clock= pygame.time.Clock()

cielo= pygame.image.load("immagini/cielo.png")
cornice2= pygame.image.load("immagini/cornice2.png")
cornicesu= pygame.transform.flip(cornice2, False, True)
nuvoletta= pygame.image.load("immagini/nuvoletta.png")
tom= pygame.image.load("immagini/tom.png")

WINDOW_SIZE= (605,500)
SCREEN= pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Talking Tom!")

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

    SCREEN.blit(cielo, (0,0))
    SCREEN.blit(cornice2, (0,348))
    SCREEN.blit(cornicesu, (-2,0))
    pygame.display.update()
    Clock.tick(60)