import pygame

SZEROKOSC_EKRANU = 1024
WYSOKOSC_EKRANU = 800

pygame.init()
ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()
obraz_tla = pygame.image.load('images/background.png')