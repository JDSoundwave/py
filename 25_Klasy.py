# Kurs programowania w języku Python

class Czlowiek:

    imie = "Kamil"
    nazwisko = "Kowal"

    def PrzedstawSie(self):

        print("Cześć mam na imię " + self.imie)

obiekt_1 = Czlowiek()

print(obiekt_1.imie)
obiekt_1.PrzedstawSie()