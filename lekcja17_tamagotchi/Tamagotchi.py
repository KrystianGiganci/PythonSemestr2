class Tamagotchi:
    def __init__(self) -> None:
        self.poziom_glodu = 50
        self.poziom_szczescia = 50

    def nakarm(self):
        self.poziom_glodu += 10
        if self.poziom_glodu > 100:
            self.poziom_glodu = 100

    def pobaw_sie(self):
        self.poziom_szczescia += 10
        if self.poziom_szczescia > 100:
            self.poziom_szczescia = 100

    def aktualizuj(self):
        self.poziom_glodu -= 0.1
        if self.poziom_glodu < 0:
            self.poziom_glodu = 0
        self.poziom_szczescia -= 0.1
        if self.poziom_szczescia < 0:
            self.poziom_szczescia = 0
