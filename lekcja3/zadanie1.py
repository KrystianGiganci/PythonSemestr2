"""
ZADANIE:
uzupełnij poniższe klasy dodając do nich konstruktor, za pomocą którego będzie można
nadać powstającym obiektom ich geometryczne wymiary (promień r, długości boku x/y).
Następnie stwórz metodę, która wyświetli pole oraz obwód tej figury.
"""
PI = 3.14


class Figura():
    def wyswietl_pole(self):
        print(f'Pole wynosi: {self.pole}')

    def wyswietl_obwod(self):
        print(f'Obwod wynosi: {self.obwod}')


class Kolo(Figura):
    def __init__(self, r):
        self.r = r
        self.obwod = 2*PI*r
        self.pole = PI*r*r


class Prostokat():
    pass

kolo1 = Kolo(15)
kolo1.wyswietl_pole()
kolo1.wyswietl_obwod()