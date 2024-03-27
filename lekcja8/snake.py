import pygame
import random
import time

SZEROKOSC_EKRANU = 800
WYSOKOSC_EKRANU = 608

pygame.init()
ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()
tlo = pygame.Surface((SZEROKOSC_EKRANU, WYSOKOSC_EKRANU))

for i in range(25):
    for j in range(19):
        obraz = pygame.image.load("images/background.png")
        maska = (random.randrange(0, 20), random.randrange(0, 20), random.randrange(0, 20))

        obraz.fill(maska, special_flags=pygame.BLEND_ADD)
        wspolrzedne = 0, 0  # TODO
        tlo.blit(obraz, wspolrzedne)

gra_dziala = True
while gra_dziala:
    # obsługa zdarzeń
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.KEYDOWN:
            # naciśnięcie klawisza ESC zamyka okno
            if zdarzenie.key == pygame.K_ESCAPE:
                gra_dziala = False
        # naciśnięcie przycisku X w górnym rogu zamyka okno
        elif zdarzenie.type == pygame.QUIT:
            gra_dziala = False


    ekran.blit(tlo, (0, 0))
    pygame.display.flip()
    zegar.tick(30)

pygame.quit()