import pygame
from Platforma import Platforma

SZEROKOSC_EKRANU = 1024
WYSOKOSC_EKRANU = 800

pygame.init()
ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()
obraz_tla = pygame.image.load('lekcja11_arkanoid/images/background.png')

platforma = Platforma()

gra_dziala = True
while gra_dziala:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                gra_dziala = False
        elif zdarzenie.type == pygame.QUIT:
            gra_dziala = False

    # sterowanie platformą
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        platforma.ruszaj_platforma(-1)
    if keys[pygame.K_RIGHT]:
        platforma.ruszaj_platforma(1)

    # rysowanie tła
    ekran.blit(obraz_tla, (0, 0))

    # rysowanie platformy
    ekran.blit(platforma.obraz, platforma.pozycja)

    pygame.display.flip()
    zegar.tick(30)

# dodanie 3 sekund opoźnienia po przegraniu
pygame.quit()
