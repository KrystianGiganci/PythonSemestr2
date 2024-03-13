"""
Klasa postać, posłuży nam na lekcji 5 -- podczas powtórki, na której stworzymy grę
Każda postać powinna mieć swoje imię, aktualny stan życia oraz maksymalny stan życia.
Pierwszą metodą, którą stworzymy dla tej klasy będzie metoda 'atakuj', dzięki której
postacie będą mogły ze sobą walczyć.
"""
from random import randint


class Postac():
    def __init__(self) -> None:
        self.nazwa = ''
        self.zycie = 1
        self.max_zycie = 1

    def atakuj(self, przeciwnik):
        obrazenia = randint(0, 3)

        if obrazenia == 0:
            print(f'{przeciwnik.nazwa} unika ataku {self.nazwa}.')
        else:
            print(f'{self.nazwa} atakuje {przeciwnik.nazwa} i zadaje jej {obrazenia} obrazen.')
            przeciwnik.zycie -= obrazenia


class Przeciwnik(Postac):
    """
    Klasa Przeciwnik powinna w konstruktorze losować
    nazwę postaci (np. goblin, szkielet, zombie...)
    oraz losować jego życie - z zakresu od 1 do
    aktualnego zdrowia gracza
    """
    pass


class Gracz(Postac):
    '''
    Klasa Gracz będzie bardziej skomplikowana niż Przeciwnik.
    Najpierw omówimy konstruktor:
        - powinien on ustawiać życie oraz maksymalne życie gracza na 10,
        - jako nazwe powinien przyjąć imię od użytkownika.
    Gracz powinien mieć też dwie inne metody:
    - odpoczynek: przywraca graczowi jeden punkt życia,
    - walka: pozwala graczowi podjąć walkę z przeciwnikiem lub przed nim uciekać.
    '''
    pass


"""
Na końcu powinna znajdować się 'główna' część gry, czyli
zainicjowanie (czyli stworzenie) gracza, a także pętla gry.
W niej gracz powinien podejmować decyzję na temat swojego ruchu:
odpoczywamy czy zwiedzamy - kontynuujemy poszukiwnie przeciwników.
Odpoczynek został już opisany w klasie Gracz, natomiast zwiedzanie
może nam dać dwa wyniki:
 1. Gracz znajdzie pustą jaskinię - wracamy do dalszych poszukiwań,
 2. Gracz natrafi na przeciwnika, z którym zaczyna walczyć.
"""