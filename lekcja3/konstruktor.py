class Samochod():
    def __init__(self, marka, model, typ_silnika, moc_KM) -> None:
        print("Utworzono obiekt klasy Samochód")
        self.marka = marka
        self.model = model
        self.typ_silnika = typ_silnika
        self.moc_KM = moc_KM
        pass

    def wyswietl(self):
        print(self.marka)
        print(self.model)
        print(self.typ_silnika)
        print(self.moc_KM)


auto1 = Samochod("Ford", 'Focus', 'Benzyna', '180')
