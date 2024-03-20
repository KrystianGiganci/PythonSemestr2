import pygame

SZEROKOSC_EKRANU = 800
WYSOKOSC_EKRANU = 600
obraz_tla = pygame.image.load('images/background.png')

pygame.init()
ekran = pygame.display.set_mode([SZEROKOSC_EKRANU, WYSOKOSC_EKRANU])
zegar = pygame.time.Clock()


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

    # rysowanie tła
    ekran.blit(obraz_tla, (0, 0))

    # wyczyszczenie ekranu
    pygame.display.flip()

    # ustalenie stałego poziomu fps
    zegar.tick(30)
# koniec pętli while

pygame.quit()
