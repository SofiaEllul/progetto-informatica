from random import randint
import pygame

nuvoletta= pygame.image.load("immagini/nuvoletta.png")
vel=6

WINDOW_SIZE= (605,500)
SCREEN= pygame.display.set_mode(WINDOW_SIZE)

class nuvolette:
    def __init__(self):
        self.x=600
        self.y=randint(-20,150)
    def movimento(self):
        self.x-=vel
        SCREEN.blit(nuvoletta, (self.x,self.y+100))