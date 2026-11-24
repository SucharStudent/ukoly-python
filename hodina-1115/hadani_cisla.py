import random

tajne_cislo = random.randint(1, 20)
pokusy = 0
tip = 0

print("Myslím si číslo od 1 do 20.")

while tip != tajne_cislo:
    tip = int(input("Zadej svůj tip: "))
    pokusy += 1

    if tip < tajne_cislo:
        print("Moje číslo je VĚTŠÍ!")
    elif tip > tajne_cislo:
        print("Moje číslo je MENŠÍ!")
    else:
        print(f"Gratuluji! Uhodl jsi číslo {tajne_cislo} na {pokusy}. pokus.")