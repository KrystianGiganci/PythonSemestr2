import pygame
from Kierunek import Kierunek


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
        self.kierunek = self.nowy_kierunek
        self.obraz = pygame.transform.rotate(self.oryginalny_obraz, (self.kierunek.value*-90))

        if self.kierunek == Kierunek.GORA:
            self.rect.move_ip(0, -32)
        if self.kierunek == Kierunek.PRAWO:
            self.rect.move_ip(32, 0)
        if self.kierunek == Kierunek.DOL:
            self.rect.move_ip(0, 32)
        if self.kierunek == Kierunek.LEWO:
            self.rect.move_ip(-32, 0)
