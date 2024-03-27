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

pygame.font.init()
moja_czcionka = pygame.font.SysFont('Comic Sans MS', 30)


def wypisz_tekst(tekst, pozycja):
    napis = moja_czcionka.render(tekst, False, (255, 255, 255))
    ekran.blit(napis, pozycja)


nakrycie_glowy = Element.NakrycieGlowy()
ubranie = Element.UbranieElement()
oczy = Element.OczyElement()
bron = Element.BronElement()
gra_dziala = True
zapisywanie = False

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
            if zdarzenie.key == pygame.K_s:
                zapisywanie = True
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

    # zapisywanie
    if zapisywanie:   # if zapisywanie == if zapisywanie is True
        pygame.image.save(ekran, 'moja_postac.png')

    # wypisywanie informacji o zmianach wyświetlanego elementu
    wypisz_tekst('[Q] - zmiana nakrycia głowy', (70, 100))
    wypisz_tekst('[W] - zmiana ubrania', (70, 130))
    wypisz_tekst('[E] - zmiana oczu', (70, 160))
    wypisz_tekst('[R] - zmiana broni', (70, 190))
    wypisz_tekst('[S] - Zapisz', (70, 220))


    # wyczyszczenie ekranu
    pygame.display.flip()

    # ustalenie stałego poziomu fps
    zegar.tick(30)
# koniec pętli while

pygame.quit()
