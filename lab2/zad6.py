litera = input("Podaj literę: ")

if litera.isupper():
    print("Wprowadzona litera jest duża.")
elif litera.islower():
    print("Wprowadzona litera jest mała.")
else:
    print("Wprowadzony znak nie jest literą (lub wprowadzono więcej znaków).")