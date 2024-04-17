import pygame
from Kierunek import Kierunek
from Segment import Segment
import copy


class Waz(pygame.sprite.Sprite):
    def __init__(self):
        # oryginalny obraz głowy, zawsze taki sam
        self.oryginalny_obraz = pygame.image.load("images/head.png")

        # obraz pomocniczy, który będzie się zmieniał w trakcie gry podczas
        # zmiany kierunku chodzenia
        self.obraz = pygame.transform.rotate(self.oryginalny_obraz, 0)

        # współrzędne głowy
        self.rect = self.obraz.get_rect(center=(12*32+16, 9*32+16))

        # zmienne odpowiedzialne za kierunek
        self.kierunek = Kierunek.GORA
        self.nowy_kierunek = Kierunek.GORA

        self.ostatnia_pozycja = self.rect

        self.dodaj_segment = False
        self.segmenty = []

    def zmien_kierunek(self, nowy_kierunek):
        zmiana_mozliwa = True
        if nowy_kierunek == Kierunek.GORA and self.kierunek == Kierunek.DOL:
            zmiana_mozliwa = False
        if nowy_kierunek == Kierunek.DOL and self.kierunek == Kierunek.GORA:
            zmiana_mozliwa = False
        if nowy_kierunek == Kierunek.LEWO and self.kierunek == Kierunek.PRAWO:
            zmiana_mozliwa = False
        if nowy_kierunek == Kierunek.PRAWO and self.kierunek == Kierunek.LEWO:
            zmiana_mozliwa = False
        if zmiana_mozliwa:
            self.nowy_kierunek = nowy_kierunek

    def aktualizuj(self):
        # poruszanie głową węża
        self.kierunek = self.nowy_kierunek
        self.obraz = pygame.transform.rotate(self.oryginalny_obraz, (self.kierunek.value*-90))

        self.ostatnia_pozycja = copy.deepcopy(self.rect)
        if self.kierunek == Kierunek.GORA:
            self.rect.move_ip(0, -32)
        if self.kierunek == Kierunek.PRAWO:
            self.rect.move_ip(32, 0)
        if self.kierunek == Kierunek.DOL:
            self.rect.move_ip(0, 32)
        if self.kierunek == Kierunek.LEWO:
            self.rect.move_ip(-32, 0)

        # poruszanie segmentami
        for i in range(len(self.segmenty)):
            if i == 0:
                self.segmenty[i].przesun(self.ostatnia_pozycja)
            else:
                self.segmenty[i].przesun(self.segmenty[i-1].ostatnia_pozycja)
            pass

        # dodawanie nowego segmentu
        if self.dodaj_segment:
            print('Tworze segment')
            nowy_segment = Segment()

            if len(self.segmenty) > 0:
                nowa_pozycja = copy.deepcopy(self.segmenty[-1].pozycja)
            else:
                nowa_pozycja = copy.deepcopy(self.ostatnia_pozycja)
            nowy_segment.pozycja = nowa_pozycja
            self.segmenty.append(nowy_segment)
            self.dodaj_segment = False

    def jedz_jablko(self):
        self.dodaj_segment = True

    def sprawdz_kolizje(self):
        # wyjście poza ekran
        if self.rect.top < 0 or self.rect.top >= 608:
            return True
        if self.rect.left < 0 or self.rect.left >= 800:
            return True

        # ugryzienie ogona
        for segment in self.segmenty:
            if self.rect.topleft == segment.pozycja.topleft:
                return True

        # jezeli nie sprawdzily sie powyzsze warunki
        return False
