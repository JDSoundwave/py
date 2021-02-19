

lista = [1, 2, "string", 3, "znaki",]

print(lista)
print("Wartość indexu:", lista[0])

lista[2] = 19 # Przypisanie nowej wartości do indexu.
print(lista)

tekst = "Hello World" # Przypisanie wartości do zmiennej -> tekst.
lista[2] = tekst # Przypisanie zmiennej -> tekst do indexu.
print(lista)

print(tekst[3]) # Wartość 3 znaku w indexie -> tekst.

print(lista + ["f", "g"]) # Dodanie indeksów do listy.
print(lista)

lista += ["f", "g"] # Trwałe dodanie indeksów do listy.
print(lista)

print("Długość elementów:", len(lista))

lista.append([33, 333, 666]) # Dodanie drugiej listy na końcu.
print(lista)
print(lista[7][1])

lista.insert(3, 7) # Dodanie wartości 7 na pozycji 3 indexu.
print(lista)

print("Ilość wystąpień:", lista.count("znaki"))
print("Nr indexu:", lista[8].index(666))

lista.remove("g")
print(lista)


lista_2 = [0, 9, 6, 4, 3, 66,]
print("Minimum:", min(lista_2))

lista_2.sort()
print(lista_2)

lista_2.reverse()
print(lista_2)

lista_2.clear()
print(lista_2)

