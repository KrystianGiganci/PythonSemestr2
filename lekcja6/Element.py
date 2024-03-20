import pygame


# klasa pomocnicza Obraz
class Obraz(pygame.sprite.Sprite):
    def __init__(self, sciezka) -> None:
        super().__init__()
        self.obraz = pygame.image.load(sciezka)


# klasa bazowa Element
class Element():
    def __init__(self, typ) -> None:
        # wskaźnik wybranego elementu ubioru
        self.wybrany = 0
        # lista obrazów
        self.lista_obrazow = []
        # wczytanie wszystkich obrazów z folderu
        for i in range(1, 4):
            sciezka = f'images/{typ}{i}.png'
            wczytany_obraz = Obraz(sciezka)
            self.lista_obrazow.append(wczytany_obraz)
