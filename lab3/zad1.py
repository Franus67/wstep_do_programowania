paliwo = 100
paliwo_zuzyte_na_s = 10
czas = 0

while paliwo > 0:
    print(f"Czas lotu: {czas} s | Pozostało paliwa: {paliwo} litrów")
    paliwo -= paliwo_zuzyte_na_s
    czas += 1

print("Konie lotu.")