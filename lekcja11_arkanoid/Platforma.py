import pygame

SZEROKOSC_EKRANU = 1024
WYSOKOSC_EKRANU = 800


class Platforma(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super(Platforma, self).__init__()
        self.obraz = pygame.image.load("lekcja11_arkanoid/images/pad.png")
        self.zresetuj_pozycje()

    def zresetuj_pozycje(self):
        self.pozycja = pygame.Rect(SZEROKOSC_EKRANU/2 - 70, WYSOKOSC_EKRANU-100, 140, 30)
