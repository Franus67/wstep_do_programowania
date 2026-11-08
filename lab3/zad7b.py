n = int(input("Podaj liczbę studentów: "))
suma_punktow = 0
dodani_studenci = 0

while True:
    if dodani_studenci == n:
        break

    punkty = float(input(f"Podaj punkty dla studenta nr {dodani_studenci + 1}: "))

    if punkty < 0 or punkty > 100:
        print("Punkty muszą być z przedziału 0 - 100. Podaj ponownie.")
        continue

    suma_punktow += punkty
    dodani_studenci += 1

print(f"Średnia punktów w grupie: {suma_punktow / n:.2f}")