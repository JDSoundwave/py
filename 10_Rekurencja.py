# Kurs programowania w języku Python

def funkcja_1(x):
    
    return x * x

zmienna = funkcja_1
print(zmienna(6))


def funkcja_2(f_1, x):

    return f_1(x) * x

print(funkcja_2(funkcja_1, 3))


# REKURENCJA


def silnia(x):

    if x <= 1:
        
        return 1
    
    else:

        return x * silnia(x - 1)

print(silnia(4))