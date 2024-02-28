class Samochod():
    liczba_kół = 4

    def __init__(self, marka, model, typ_silnika, moc_KM):  # to jest konstruktor
        print("Utworzono obiekt klasy Samochód")
        self.licznik2 = 9
        Samochod.licznik1 += 1
        self.marka = marka              # to jest zmienna naszego obiektu
        self.model = model              # to jest zmienna naszego obiektu
        self.typ_silnika = typ_silnika  # to jest zmienna naszego obiektu
        self.moc_KM = moc_KM            # to jest zmienna naszego obiektu
        pass

    def wyswietl(self):  # to jest metoda o nazwie wyswietl
        print(self.marka)
        print(self.model)
        print(self.typ_silnika)
        print(self.moc_KM)



auto1 = Samochod("Ford", 'Focus', 'Benzyna', 180)  # konstruktor wywołuje się podczas tej linijki
                                                     # czyli utworzenia obiektu klasy

auto2 = Samochod('Mazda', '6', 'Benzyna', 240)
print(auto1.licznik1, auto2.licznik1)
