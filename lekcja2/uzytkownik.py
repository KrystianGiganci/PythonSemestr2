class Uzytkownik():
    imie = ""
    nazwisko = ""
    wiek = 0

    def wyswietl_info(self):
        print(f"{self.imie} ma {self.wiek} lat.")

    def zmien_wiek(self, nowy_wiek):
        self.wiek = nowy_wiek

    def zmien_imie(self, nowe_imie):
        self.imie = nowe_imie
