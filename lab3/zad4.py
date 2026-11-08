liczba_gosc = int(input("Podaj liczbę gości: "))
liczba_potraw = int(input("Podaj liczbę zamówionych dań: "))

suma_rachunku = 0
i = 1

while i <= liczba_potraw:
    cena = float(input(f"Podaj cenę potrawy nr {i}: "))
    suma_rachunku += cena
    i += 1

srednia_cena = suma_rachunku / liczba_potraw
koszt_na_osobe = suma_rachunku / liczba_gosc

print(f"\nŚrednia cena potrawy: {srednia_cena:.2f} zł")
print(f"Całkowity rachunek: {suma_rachunku:.2f} zł")
print(f"Każdy z gości musi zapłacić: {koszt_na_osobe:.2f} zł")