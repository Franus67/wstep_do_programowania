print("a)")
with open("notowania_gieldowe.txt", "r") as plik:
    for linia in plik:
        print(linia)

with open("notowania_gieldowe.txt", "a") as plik:
    plik.write("\nALR, 113")

print("b)")
with open("notowania_gieldowe.txt", "r") as plik:
    for linia in plik:
        print(linia)