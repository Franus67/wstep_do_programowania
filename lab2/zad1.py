punkty = float(input("Podaj liczbę zdobytych punktów: "))

if punkty > 80:
    print("Gratulacje zaliczyłeś egzamin w terminie 0.")
elif punkty >= 50:
    print("Zdobyłeś od 50 do 80 punktów. Możesz poprawić swój wynik.")
else:
    print("Zdobyłeś poniżej 50 punktów. Musisz poprawić egzamin.")