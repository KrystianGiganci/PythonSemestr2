import pygame
import random
import time

SZEROKOSC_EKRANU = 800
WYSOKOSC_EKRANU = 608

tlo = pygame.Surface((SZEROKOSC_EKRANU, WYSOKOSC_EKRANU))

for i in range(25):
    for j in range(19):
        obraz = pygame.image.load("images/background.png")
        maska = (random.randrange(0, 20), random.randrange(0, 20), random.randrange(0, 20))

        obraz.fill(maska, special_flags=pygame.BLEND_ADD)
        wspolrzedne = 0, 0  # TODO
        tlo.blit(obraz, wspolrzedne)