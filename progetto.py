import pygame, sys
from random import randint
from pygame.locals import *

pygame.init()
Clock= pygame.time.Clock()

cielo= pygame.image.load("immagini/cielo.png")
cornice= pygame.image.load("immagini/cornice.png")
nuvoletta= pygame.image.load("immagini/nuvoletta.png")
tom= pygame.image.load("immagini/tom.png")

WINDOW_SIZE= (700,500)
SCREEN= pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Talking Tom!")

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

    SCREEN.blit(cielo, (0,0))
    SCREEN.blit(cornice, (0,0))

    pygame.display.update()
    Clock.tick(60)
