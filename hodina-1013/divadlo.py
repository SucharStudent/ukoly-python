# zakladni udaje
pocet_osob=int(input("Kolik vás je? : "))
vek=int(input("Kolik vám je let? : "))
student=str(input("jste student? : "))

# ceny vstupenek
cena=500

# zjistovani skupinove slevy
if pocet_osob >= 4 :
    cena*= 0.75
    print("Získaly jste skupinovou slevu!")
    
# zjistovani studentske slevy
elif vek<26 and student in ("ano" "Ano" "ANO") :
    cena *= 0.7
    print("Máte studentskou slevu!")


# zjistovani seniorske slevy
elif vek>= 65 :
    cena *=0.8
    print("Získaly jste seniorskou slevu slevu!")

# vypocet vysledne ceny
vysledna_cena = cena * pocet_osob
print(f"Cena za jednu vstupenku: {cena} Kč")
print(f"Všechny vstupenky vás budou stát celkem: {vysledna_cena} Kč")