class Zwierze():  # klasa bazowa
    def __init__(self, wiek, imie):  # konstruktor klasy bazowej
        self.wiek = wiek
        self.imie = imie

    def wydaj_dzwiek(self):
        print(f'{self.imie} wydaje dzwięk')

    def jedz(self):
        print(f'{self.imie} je')

# Klasa bazowa - Zwierze
# Klasa pochodna - Pies
class Pies(Zwierze): # klasa pochodna Pies, ktora dziedziczy po klasie Zwierze
    def __init__(self, wiek, imie, kolor_siersci):
        super().__init__(wiek, imie)
        self.kolor_siersci = kolor_siersci

    def wypisz_kolor(self):
        print(f'{self.imie} ma siersc, ktorej kolor to: {self.kolor_siersci}')


class Kot(Zwierze):
    def __init__(self, wiek, imie, ulubione_miejsce_do_spania):
        super().__init__(wiek, imie)
        self.ulubione_miejsce_do_spania = ulubione_miejsce_do_spania

    def poloz_sie_spac(self):
        print(f'{self.imie} kładzie się spać w tym miejscu: {self.ulubione_miejsce_do_spania}')


zwierze1 = Kot(8, 'Azor', 'wanna')
print(type(zwierze1))
zwierze1.wydaj_dzwiek()
zwierze1.jedz()
zwierze1.poloz_sie_spac()
