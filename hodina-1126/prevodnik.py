# Pomocna funkce pro prevod cislice na znak
def cifra_na_znak(hodnota):
    if hodnota >= 0 and hodnota <= 9:
        return str(hodnota)
    elif hodnota >= 10 and hodnota <= 15:
        pismena = ["A", "B", "C", "D", "E", "F"]
        return pismena[hodnota - 10]


# Funkce pro prevod do jine ciselne soustavy
def preved_soustavu(cislo, zaklad):

    if cislo < 0:
        return None

    if zaklad != 2 and zaklad != 8 and zaklad != 10 and zaklad != 16:
        return None

    if cislo == 0:
        return "0"

    vysledek = ""

    while cislo > 0:
        zbytek = cislo % zaklad
        cifra = cifra_na_znak(zbytek)

        vysledek = cifra + vysledek
        cislo = cislo // zaklad

    return vysledek


# Hlavni program

print("DEC | BIN | OCT | DEC | HEX")
print("----------------------------")

cislo = 0

while cislo <= 20:

    binarni = preved_soustavu(cislo, 2)
    osmickova = preved_soustavu(cislo, 8)
    desitkova = preved_soustavu(cislo, 10)
    sestnactkova = preved_soustavu(cislo, 16)

    print(str(cislo).ljust(3), "|",
          binarni.ljust(5), "|",
          osmickova.ljust(3), "|",
          desitkova.ljust(3), "|",
          sestnactkova)

    cislo = cislo + 1


print()
print("Test neplatneho cisla:", preved_soustavu(-5, 2))
print("Test neplatneho zakladu:", preved_soustavu(10, 5))