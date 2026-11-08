
imie = input("Podaj imię: ")
print(f"Witaj {imie}")


wiek = input("Podaj swój wiek: ")
print(f"Twój wiek to: {wiek}")


dane = input("Podaj imię i nazwisko (rozdzielone spacją): ").split()
if len(dane) >= 2:
    inicjaly = dane[0][0].upper() + dane[1][0].upper()
    print(f"Twoje inicjały: {inicjaly}")


lancuch_5 = input("Podaj tekst do pomnożenia: ")
print(lancuch_5 * 5)


lan1 = input("Podaj pierwszy łańcuch: ")
lan2 = input("Podaj drugi łańcuch: ")
lan3 = lan1 + lan2
print(f"Połączone łańcuchy: {lan3}")


polowa = len(lan1) // 2
lan4 = lan1[:polowa] + lan2
print(f"Pierwsza połowa pierwszego + drugi: {lan4}")