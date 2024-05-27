from random import randint
import pygame

nuvoletta= pygame.image.load("immagini/nuvoletta.png")
vel=6

WINDOW_SIZE= (605,500)
SCREEN= pygame.display.set_mode(WINDOW_SIZE)

class nuvolette:
    def __init__(self):
        self.x=600
        self.y=randint(100,400)
        self.image=nuvoletta
        self.rect=pygame.transform.rotozoom(self.image, 0, 0.8).get_rect(center=(self.x, self.y))
    def movimento(self):
        self.rect.x-=vel
        SCREEN.blit(self.image, self.rect)