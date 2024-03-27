# zaimportowanie modułu pygame
import pygame
# zaimportowanie stworzonego przez nas pliku
import Element

SZEROKOSC_EKRANU = 800
WYSOKOSC_EKRANU = 600
obraz_tla = pygame.image.load('images/background.png')
obraz_bazy_postaci = pygame.image.load('images/base.png')

pygame.init()
ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()

nakrycie_glowy = Element.NakrycieGlowy()
ubranie = Element.UbranieElement()
oczy = Element.OczyElement()
bron = Element.BronElement()
gra_dziala = True

while gra_dziala:
    # obsługa zdarzeń
    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.KEYDOWN:
            # naciśnięcie klawisza ESC zamyka okno
            if zdarzenie.key == pygame.K_ESCAPE:
                gra_dziala = False
            if zdarzenie.key == pygame.K_q:
                nakrycie_glowy.wybierzNastepny()
            if zdarzenie.key == pygame.K_w:
                ubranie.wybierzNastepny()
            if zdarzenie.key == pygame.K_e:
                oczy.wybierzNastepny()
            if zdarzenie.key == pygame.K_r:
                bron.wybierzNastepny()
        # naciśnięcie przycisku X w górnym rogu zamyka okno
        elif zdarzenie.type == pygame.QUIT:
            gra_dziala = False

    # rysowanie tła
    ekran.blit(obraz_tla, (0, 0))

    # rysowanie bazy postaci
    ekran.blit(obraz_bazy_postaci, (270, 130))

    # rysowanie elementów postaci
    ekran.blit(ubranie.wybranyObraz(), (270, 130))
    ekran.blit(oczy.wybranyObraz(), (270, 130))
    ekran.blit(nakrycie_glowy.wybranyObraz(), (270, 130))
    ekran.blit(bron.wybranyObraz(), (270, 130))

    # wyczyszczenie ekranu
    pygame.display.flip()

    # ustalenie stałego poziomu fps
    zegar.tick(30)
# koniec pętli while

pygame.quit()
