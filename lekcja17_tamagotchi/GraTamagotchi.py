import sys
import pygame
from Tamagotchi import Tamagotchi

pygame.display.init()
pygame.font.init()
SZEROKOSC, WYSOKOSC = 400, 450
ekran = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))
pygame.display.set_caption("Tamagotchi")

zegar = pygame.time.Clock()

""" ! ruszamy dopiero pod koniec zajęć !
wesoly = pygame.image.load('happy.jpg')
wesoly = pygame.transform.scale(wesoly, (150, 150))
neutralny = pygame.image.load('neutral.jpg')
neutralny = pygame.transform.scale(neutralny, (150, 150))
smutny = pygame.image.load('sad.jpg')
smutny = pygame.transform.scale(smutny, (150, 150))
"""
# Kolory
kolor_tla = (130, 225, 155)
KOLOR_CZARNY = (0, 0, 0)
KOLOR_BIALY = (255, 255, 255)
KOLOR_ZIELONY = (0, 255, 0)
KOLOR_ZOLTY = (255, 255, 0)
KOLOR_CZERWONY = (255, 0, 0)

# Czcionka
CZCIONKA = pygame.font.SysFont("Comic Sans", 20)

# Inicjalizjacja Tamagotchi
tamagotchi = Tamagotchi()

# Główna pętla gry
gra_dziala = True
while gra_dziala:
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                gra_dziala = False
        elif zdarzenie.type == pygame.QUIT:
            gra_dziala = False
    tamagotchi.aktualizuj()

    ekran.fill(kolor_tla)
    # Interfejs
    ## pasek szczescia
    szerokosc_paska_szczescie = tamagotchi.poziom_szczescia
    pygame.draw.rect(ekran, KOLOR_CZARNY, pygame.Rect(50, 50, szerokosc_paska_szczescie, 20))
    tekst_szczescie = CZCIONKA.render("Szczęście:", True, KOLOR_CZARNY)
    ekran.blit(tekst_szczescie, (50, 20))
    ## pasek głodu
    szerokosc_paska_glodu = tamagotchi.poziom_glodu
    pygame.draw.rect(ekran, KOLOR_CZARNY, pygame.Rect(50, 100, szerokosc_paska_glodu, 20))
    tekst_glod = CZCIONKA.render("Poziom głodu:", True, KOLOR_CZARNY)
    ekran.blit(tekst_glod, (50, 70))

    """ ! ruszamy dopiero pod koniec zajęć !
    nastroj = tamagotchi.poziom_glodu + tamagotchi.poziom_szczescia
    if nastroj > 120:
        ekran.blit(wesoly, (125, 135))
    elif nastroj > 60:
        ekran.blit(neutralny, (125, 135))
    else:
        ekran.blit(smutny, (125, 135))
    """
    pygame.display.flip()
    zegar.tick(30)

pygame.quit()