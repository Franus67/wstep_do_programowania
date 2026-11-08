znalezione = 0
liczba = 2
wynik = []

while True:
    czy_pierwsza = True
    for i in range(2, int(liczba ** 0.5) + 1):
        if liczba % i == 0:
            czy_pierwsza = False
            break

    if czy_pierwsza:
        wynik.append(str(liczba))
        znalezione += 1

    if znalezione == 10:
        break

    liczba += 1

print(",".join(wynik))