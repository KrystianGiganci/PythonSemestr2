import pygame
import random
from Platforma import Platforma
from Kulka import Kulka
from Klocek import Klocek

SZEROKOSC_EKRANU = 1024
WYSOKOSC_EKRANU = 800
Poziom = 0
Zycia = 10

poziom1 = [
    [0, 1, 2, 3, 5, 1, 2, 3, 2, 4],
    [0, 1, 2, 3, 5, 1, 2, 3, 2, 4],
    [0, 1, 2, 3, 5, 1, 2, 3, 2, 4],
    [0, 1, 2, 3, 5, 1, 2, 3, 2, 4],
    [0, 1, 2, 3, 5, 1, 2, 3, 2, 4],
    [0, 1, 2, 3, 5, 1, 2, 3, 2, 4],
    [0, 1, 2, 3, 5, 1, 2, 3, 2, 4],
]
poziom2 = [
    [0, 1, 2, 3, 5, 1, 2, 3, 2, 4],
    [0, 1, 2, 3, 5, 1, 2, 3, 2, 4],
    [0, 1, 2, 3, 5, 1, 2, 3, 2, 4],
    [0, 1, 2, 3, 5, 1, 2, 3, 2, 4],
    [0, 1, 2, 3, 5, 1, 2, 3, 2, 4],
    [0, 1, 2, 3, 5, 1, 2, 3, 2, 4],
    [0, 1, 2, 3, 5, 1, 2, 3, 2, 4],
]
poziom3 = [
    [random.randint(1, 10), random.randint(1, 12), random.randint(1, 15), random.randint(1, 20), random.randint(1, 30), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)],
    [random.randint(1, 10), random.randint(1, 12), random.randint(1, 15), random.randint(1, 20), random.randint(1, 30), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)],
    [random.randint(1, 10), random.randint(1, 12), random.randint(1, 15), random.randint(1, 20), random.randint(1, 30), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)],
    [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)],
    [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)],
    [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)],
    [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
]

pygame.init()
pygame.font.init()
czcionka = pygame.font.SysFont('Comic Sans MS', 25)
ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()
obraz_tla = pygame.image.load('lekcja11_arkanoid/images/background.png')

platforma = Platforma()
kulka = Kulka()
klocki = pygame.sprite.Group()


def dodaj_klocki():
    wczytany_poziom = None
    if Poziom == 0:
        wczytany_poziom = poziom1
    if Poziom == 1:
        wczytany_poziom = poziom2
    if Poziom == 2:
        wczytany_poziom = poziom3

    for i in range(10):
        for j in range(7):
            if wczytany_poziom[j][i] != 0:
                x = i*96 + 32
                y = j*48 + 32
                zdrowie = wczytany_poziom[j][i]
                klocek = Klocek(x, y, zdrowie)
                klocki.add(klocek)


dodaj_klocki()
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

    # sprawdzenie czy wszystkie klocki zostały zniszczone
    # i ewentualnie ładowanie nowego poziomu
    if len(klocki.sprites()) == 0:
        Poziom += 1
        if Poziom >= 3:
            break
        kulka.zresetuj_pozycje()
        platforma.zresetuj_pozycje()
        dodaj_klocki()

    kulka.aktualizuj(platforma, klocki)
    klocki.update()
    platforma.aktualizuj()

    if kulka.przegrana:
        Zycia -= 1
        if Zycia <= 0:
            pygame.quit()
        kulka.zresetuj_pozycje()
        platforma.zresetuj_pozycje()

    # rysowanie tła
    ekran.blit(obraz_tla, (0, 0))

    # rysowanie klocków
    for klocek in klocki:
        ekran.blit(klocek.obraz, klocek.pozycja)

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
