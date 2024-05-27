from random import randint
import pygame

monetina=pygame.image.load('immagini/monetina.png')
vel=6

WINDOW_SIZE= (605,500)
SCREEN= pygame.display.set_mode(WINDOW_SIZE)


class monetine:
    def __init__(self):
        self.x=400
        self.y=randint(-10,150)
    def movimento(self):
        self.x-=vel
        SCREEN.blit(monetina, (self.x,self.y+100))

