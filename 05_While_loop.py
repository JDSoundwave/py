# Kurs programowania w języku Python

x = 0

print(x)

while x <= 50:

    x += 1

    if x % 2 == 1:
        continue

    print(x)

    if x >= 30:
        break


print("KONIEC")