print("Mysli si číslo od 1 do 100. Odpovídej: v (větší), m (menší), s (správně).")

dole = 1
nahore = 100
pokusy = 0
odpoved = ""

while odpoved != "s":
    tip = (dole + nahore) // 2
    pokusy += 1
    print(f"Je tvé číslo {tip}?")
    odpoved = input("Zadej v / m / s: ")

    if odpoved == "v":
        dole = tip + 1
    elif odpoved == "m":
        nahore = tip - 1

print(f"Uhodl jsem to na {pokusy}. pokus!")