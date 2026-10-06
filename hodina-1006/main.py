 # Polarita proměnné 
 
cislo = float(input("Zadejte číslo: "))
    
if cislo > 0:
    print("Zadané číslo je kladné.")
elif cislo == 0:
    print("Zadané číslo je nula.")
else:
    print("Zadané číslo je záporné.")
    cislo = -cislo

print(f"Absolutní hodnota je {cislo}")