cas= float(input("Zadejte čas: "))

if cas < 0:
    print("Čas nemůže být záporný.")
elif cas < 6 :
    print("Dobrou noc!")

elif cas < 9:
    print("Dobré ráno!")

elif cas < 12:
    print("Dobré dopoledne!")

elif cas < 17:
    print("Dobré odpoledne!")

elif cas < 2:
    print("Dobrý večer!")

elif cas > 24:
    print("Čas nemůže být větší než 24 hodin.")

