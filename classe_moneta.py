from random import randint
import pygame

monetina=pygame.image.load('immagini/monetina.png')
vel=6

WINDOW_SIZE= (605,500)
SCREEN= pygame.display.set_mode(WINDOW_SIZE)


class monetine:
    def __init__(self):
        self.x=600
        self.y=randint(50,450)
        self.image=monetina
        self.rect=self.image.get_rect(center=(self.x, self.y))
    def movimento(self):
        self.rect.x-=vel
        SCREEN.blit(self.image, self.rect)

