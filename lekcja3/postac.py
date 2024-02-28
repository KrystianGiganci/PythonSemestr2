"""
Klasa postać, posłuży nam na lekcji 5 -- podczas powtórki, na której stworzymy grę
Każda postać powinna mieć swoje imię, aktualny stan życia oraz maksymalny stan życia.
Pierwszą metodą, którą stworzymy dla tej klasy będzie metoda 'atakuj', dzięki której
postacie będą mogły ze sobą walczyć.
"""
from random import randint


class Postac():
    def __init__(self, nazwa, zycie, max_zycie) -> None:
        self.nazwa = nazwa
        self.zycie = zycie
        self.max_zycie = max_zycie

    def atakuj(self, przeciwnik):
        obrazenia = randint(0, 3)

        if obrazenia == 0:
            print(f'{przeciwnik.nazwa} unika ataku {self.nazwa}.')
        else:
            print(f'{self.nazwa} atakuje {przeciwnik.nazwa} i zadaje jej {obrazenia} obrazen.')
            przeciwnik.zycie -= obrazenia
