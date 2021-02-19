# Zadanie nr 1

def dane(imie, nazwisko):

        dane = imie[0].upper + '.' + nazwisko
        return dane

x = input('Podaj swoje imię: ')

y = input('Podaj swoje nazwisko: ')

print(dane(x, y))