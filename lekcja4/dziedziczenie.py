class Zwierze():  # klasa bazowa
    def __init__(self, wiek, imie):  # konstruktor klasy bazowej
        self.wiek = wiek
        self.imie = imie

    def wydaj_dzwiek(self):
        print(f'{self.imie} wydaje dzwięk')

    def jedz(self):
        print(f'{self.imie} je')


class Pies(Zwierze): # klasa pochodna Pies, ktora dziedziczy po klasie Zwierze
    def __init__(self, wiek, imie, kolor_siersci):
        super().__init__(wiek, imie)
        self.kolor_siersci = kolor_siersci

    def wypisz_kolor(self):
        print(f'{self.imie} ma siersc, ktorej kolor to: {self.kolor_siersci}')


zwierze1 = Pies(8, 'Azor', 'czarny')
print(type(zwierze1))
zwierze1.wydaj_dzwiek()
zwierze1.jedz()
zwierze1.wypisz_kolor()
