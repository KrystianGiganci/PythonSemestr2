import pygame
from Platforma import Platforma
from Kulka import Kulka

SZEROKOSC_EKRANU = 1024
WYSOKOSC_EKRANU = 800
Zycia = 10

pygame.init()
pygame.font.init()
czcionka = pygame.font.SysFont('Comic Sans MS', 25)
ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()
obraz_tla = pygame.image.load('lekcja11_arkanoid/images/background.png')

platforma = Platforma()
kulka = Kulka()

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

    kulka.aktualizuj(platforma)
    platforma.aktualizuj()

    if kulka.przegrana:
        Zycia -= 1
        if Zycia <= 0:
            pygame.quit()
        kulka.zresetuj_pozycje()
        platforma.zresetuj_pozycje()

    # rysowanie tła
    ekran.blit(obraz_tla, (0, 0))

    # rysowanie platformy i kulki
    ekran.blit(platforma.obraz, platforma.pozycja)
    ekran.blit(kulka.obraz, kulka.pozycja)

    # wyświetlenie żyć
    tekst = czcionka.render(f'Pozostałe życia: {Zycia}', False, (245, 66, 212))
    ekran.blit(tekst, (10, 10))

    pygame.display.flip()
    zegar.tick(30)

# dodanie 3 sekund opoźnienia po przegraniu

pygame.quit()
