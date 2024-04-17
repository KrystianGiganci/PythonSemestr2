import pygame
import random
import time
from Kierunek import Kierunek
from Waz import Waz
from Jablko import Jablko

SZEROKOSC_EKRANU = 800
WYSOKOSC_EKRANU = 608

pygame.init()
ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()
tlo = pygame.Surface((SZEROKOSC_EKRANU, WYSOKOSC_EKRANU))

# Waz
waz = Waz()
PORUSZ_WEZEM = pygame.USEREVENT + 1
pygame.time.set_timer(PORUSZ_WEZEM, 200)

# Jablko
jablko = Jablko()
jablka = pygame.sprite.Group()
jablka.add(jablko)

# kratka ma 32 x 32
for i in range(25):
    for j in range(19):
        obraz = pygame.image.load("images/background.png")
        maska = (random.randrange(0, 20), random.randrange(0, 20), random.randrange(0, 20))

        obraz.fill(maska, special_flags=pygame.BLEND_ADD)
        wspolrzedne = i*32, j*32  # TODO
        tlo.blit(obraz, wspolrzedne)

gra_dziala = True
while gra_dziala:
    # obsługa zdarzeń
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.KEYDOWN:
            # naciśnięcie klawisza ESC zamyka okno
            if zdarzenie.key == pygame.K_ESCAPE:
                gra_dziala = False
            if zdarzenie.key == pygame.K_w or zdarzenie.key == pygame.K_UP:
                waz.zmien_kierunek(Kierunek.GORA)
            if zdarzenie.key == pygame.K_a:
                waz.zmien_kierunek(Kierunek.LEWO)
            if zdarzenie.key == pygame.K_s:
                waz.zmien_kierunek(Kierunek.DOL)
            if zdarzenie.key == pygame.K_d:
                waz.zmien_kierunek(Kierunek.PRAWO)
        elif zdarzenie.type == PORUSZ_WEZEM:
            waz.aktualizuj()
        # naciśnięcie przycisku X w górnym rogu zamyka okno
        elif zdarzenie.type == pygame.QUIT:
            gra_dziala = False

    # sprawdzenie czy głowa węża jest na jabłku
    kolizja_z_jablkiem = pygame.sprite.spritecollideany(waz, jablka)
    if kolizja_z_jablkiem is not None:
        kolizja_z_jablkiem.kill()
        waz.jedz_jablko()
        jablko = Jablko()
        jablka.add(jablko)

    # rysowanie tła
    ekran.blit(tlo, (0, 0))

    # rysowanie jabłek
    for jablko in jablka:
        ekran.blit(jablko.obraz, jablko.rect)

    # rysowanie głowy węża
    ekran.blit(waz.obraz, waz.rect)

    # rysowanie segmentów
    for segment in waz.segmenty:
        ekran.blit(segment.obraz, segment.pozycja)

    pygame.display.flip()
    zegar.tick(30)

# dodanie 3 sekund opoźnienia po przegraniu
time.sleep(3)
pygame.quit()
