# KONROLA PRVOCISLA
import math


je_prvocislo = True

print("Kontrola prvočísla")
cislo = int(input("Zadejte celé číslo: "))

if cislo < 2:
    je_prvocislo = False
elif cislo == 2:
    je_prvocislo = True
elif cislo % 2 == 0:
    je_prvocislo = False
else:
    delitel=3
    while delitel <=math.sqrt(cislo):
        if cislo % delitel == 0:
            je_prvocislo = False
            break 
        delitel += 2

if je_prvocislo:
    print(f"Čislo {cislo} je prvočíslo")
else:
    print(f"Čislo {cislo} není prvočíslo")
