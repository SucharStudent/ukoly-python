# *****************************************
# Projekt: Kalkulačka spropitného
# Autor: Vuk Suchý
# *****************************************

print("Vítejte v kalkulačce spropitného!")

celkova_castka = float(input("Zadejte celkovou částku účtu: "))
spropitne = int(input("Zadejte spropitné v procentech: "))
pocet_osob = int(input("Zadejte počet osob u stolu: "))  

spropitne_Kc = celkova_castka * (spropitne / 100)

celkova_castka += spropitne_Kc # složene přiřazení

# celkova_castka = celkova_castka + spropitne_Kc
zaplacena_castka = round(celkova_castka / pocet_osob, 2)
print(f"Každý člověk by měl dát: {zaplacena_castka} Kč ty chudáku" )