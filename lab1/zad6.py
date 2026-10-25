import random

droga = random.randint(1, 1000)
spalanie = float(input("Podaj średnie spalanie (l/100 km): "))
cena_paliwa = float(input("Podaj aktualną cenę paliwa (zł/l): "))

zuzycie = (droga / 100) * spalanie
koszt = zuzycie * cena_paliwa

print(f"Droga do pokonania: {droga} km")
print(f"Przewidywane zużycie paliwa: {zuzycie:.2f} l")
print(f"Szacowany koszt podróży: {koszt:.2f} zł")