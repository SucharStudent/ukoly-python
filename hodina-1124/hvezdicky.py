def ctverec(strana):
    radek = 0
    while radek < strana:
        print("*" * strana)
        radek += 1

def obdelnik(a, b):
    radek = 0
    while radek < b:
        print("*" * a)
        radek += 1

def nevyplneny_obdelnik(a, b):
    radek = 0
    while radek < b:
        if radek == 0 or radek == b - 1:
            print("*" * a)
        else:
            print("*" + " " * (a - 2) + "*")
        radek += 1

def pravouhly_trojuhelnik(vyska):
    radek = 1
    while radek <= vyska:
        print("*" * radek)
        radek += 1

print("VÍTEJ V PROGRAMU PRO KRESLENÍ GEOMETRICKÝCH TVARŮ")
print()

dalsi = "ano"
while dalsi == "ano":
    tvar = input("Jaký obrazec chceš vykreslit? ").lower()
    print()
    
    if tvar == "c":
        ctverec(5)
    elif tvar == "o":
        obdelnik(5, 2)
    elif tvar == "on":
        nevyplneny_obdelnik(5, 4)
    elif tvar == "tp":
        pravouhly_trojuhelnik(5)
    else:
        print("Neznámý obrazec.")
        
    print()
    dalsi = input("Chceš vykreslit další obrazec? ").lower()
    print()

print("DĚKUJI ZA POUŽITÍ PROGRAMU")