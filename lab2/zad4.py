gol = int(input("Podaj liczbę zdobytych goli: "))

bonus = 0
if gol > 10:
    bonus = 10
elif gol > 5:
    bonus = 5

calkowity_wynik_a = (gol * 10) + bonus
print(f"a) Całkowity wynik drużyny: {calkowity_wynik_a}")

bonus = 0
if gol > 5:
    bonus += 5
if gol > 10:
    bonus += 10

calkowity_wynik_b = (gol * 10) + bonus
print(f"b) Całkowity wynik drużyny z sumowanymi bonusami: {calkowity_wynik_b}")