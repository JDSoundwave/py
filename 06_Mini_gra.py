# Kurs programowania w języku Python

from random import randint

los = randint(1, 10)

i = 0

while i != los:
    
    i += 1

    odp = int(input("Podaj liczbe od 1 do 10: "))

    if odp > los:
        print("Podałeś za dużą liczbę.")

    elif odp < los:
        print("Podałeś za małą liczbę.")

    else:
        print("BRAWO TRAFIŁEŚ !!!")

print("Wygrałeś w ",i," próbie.")