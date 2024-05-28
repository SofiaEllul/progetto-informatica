import pygame

Colore = (252, 20, 221)

class Punteggio:
    def __init__(self, screen, posizione, dimensione):
        self.screen = screen
        self.posizione = posizione
        self.dimensione = dimensione

        self.punti=0

        self.rect = pygame.Rect(posizione[0], posizione[1], dimensione[0], dimensione[1])

    def disegna(self):

        font = pygame.font.Font(None, 65)
        text = font.render(str(self.punti), 1, Colore)
        self.screen.blit(text, (40, 40))
        