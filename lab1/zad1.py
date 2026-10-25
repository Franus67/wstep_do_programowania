
print("Czesc A:")
print(1 + 2, type(1 + 2))             # +  dodawanie, wynik to liczba całkowita (int)
print(1 + 4.5, type(1 + 4.5))         # + dodawanie całkowitej i ułamka daje ułamek (float)
print(3 / 2, type(3 / 2))             # / to dzielenie, wynik  ma po przecinku, to ułamek (float)
print(4 / 2, type(4 / 2))             # / nawet jak dzieli się równo, wynik to dalej ułamek 2.0 (float)
print(3 // 2, type(3 // 2))           # // to dzielenie bez reszty, odcina to co po przecinku (int)
print(-3 // 2, type(-3 // 2))         # // dla liczb na minusie zaokrągla w dół, daje -2 (int)
print(11 % 2, type(11 % 2))           # % to reszta z dzielenia, 11 na 2 to 5 i zostaje 1 reszty (int)
print(2 ** 10, type(2 ** 10))         # ** to potęgowanie, czyli 2 do potęgi 10 (int)
print(8 ** (1/3), type(8 ** (1/3)))   # ** ułamek w potędze działa jak pierwiastek 3 stopnia (float)

print()


print("Czesc B:")
print(int(3.0), type(int(3.0)))       # int() ucina część po przecinku i robi z ułamka liczbę całkowitą
print(float(3), type(float(3)))       # float() przerabia całkowitą na ułamek, dodając do niej 0
print(float("3"), type(float("3")))   # float() potrafi przerobić słowo (tekst "3") na prawdziwy ułamek 3.0
print(str(12.4), type(str(12.4)))     # str() działa odwrotnie - robi z liczby ułamkowej zwykły tekst
print(bool(0), type(bool(0)))         # bool() sprawdza czy prawda czy fałsz. Zero (0) to w Pythonie fałsz (False)