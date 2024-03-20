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

    def wybierzNastepny(self):
        self.wybrany += 1
        if self.wybrany > 2:
            self.wybrany = 0

    def wybranyObraz(self):
        return self.lista_obrazow[self.wybrany].obraz


class NakrycieGlowy(Element):
    def __init__(self) -> None:
        super().__init__('head')


class UbranieElement(Element):
    def __init__(self) -> None:
        super().__init__('body')


class OczyElement(Element):
    def __init__(self) -> None:
        super().__init__('eye')


class BronElement(Element):
    def __init__(self) -> None:
        super().__init__('weapon')
