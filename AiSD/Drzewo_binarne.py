
# Reprezentacja jednego kółka

class Splot():
    def __init__(self, dane = None):

        # Dane - to co wkładamy do kółka.

        self.dane = dane 

        # Lewa i prawa strzałka.

        self.left_child = None
        self.right_child = None

# Struktura drzewa.

class Binary_tree():
    def __init__(self):

        # Pole korzeń jako pojedyńczy węzeł z domyślnymi wartościami.

        self.root = Splot()

    # Dostawiany element trafia w odpowiednie miejsce.

    def dodaj(self, dane):

        # Jeśli korzeń jest pusty ( nic nie wstawiliśmy).

        if self.root.dane == None:

            # Pierwsza liczba trafia do korzenia.

            self.root.dane = dane

        # Jęśli korzeń jest pełny szukamy wolnego miejsca.

        else:

            # Funkcja pomocnicza

            def add_to_vertex(dane, vertex):

                # Jeśli otrzymane dane są < dane przechowywane przez wierzchołek

                if dane < vertex.dane:
                    if vertex.left_child == None:
                        vertex.left_child = Splot(dane)
                    else:
                        add_to_vertex(dane, vertex.left_child)

                # Jeśli otrzymane dane są > dane przechowywane przez wierzchołek

                if dane > vertex.dane:
                    if vertex.right_child == None:
                       vertex.right_child = Splot(dane)
                    else:
                        add_to_vertex(dane, vertex.right_child)

            add_to_vertex(dane, self.root) # Korzeń jako pierwszy wierzchołek

    def pokaz(self):

        wynik = ''

        def Pre_order(wynik, vertex):
            if vertex:
                if vertex.dane:
                    wynik += (str(vertex.dane) + '-')
                    wynik = Pre_order(wynik, vertex.left_child)
                    wynik = Pre_order(wynik, vertex.right_child) 
            return wynik

        def In_order(wynik, vertex):
            if vertex:
                if vertex.dane:
                    wynik = In_order(wynik, vertex.left_child)
                    wynik += (str(vertex.dane) + '-')
                    wynik = In_order(wynik, vertex.right_child) 
            return wynik

        def Post_order(wynik, vertex):
            if vertex:
                if vertex.dane:
                    wynik = Post_order(wynik, vertex.left_child)
                    wynik = Post_order(wynik, vertex.right_child) 
                    wynik += (str(vertex.dane) + '-')
            return wynik
            
        print(Pre_order(wynik, self.root))
        print(In_order(wynik, self.root))
        print(Post_order(wynik, self.root))

drzewo = Binary_tree()

drzewo.left_child(6)

drzewo.pokaz()