#vypis promennych
a = int(input("Zadejte číslo A: "))
b = int(input("Zadejte číslo B: "))
c = int(input("Zadejte číslo C: "))

#predpokladame ze prvni cislo "a" bude minimum a maximum
min_val = a
max_val = a

# porovname s druhym cislem "b"
if b<min_val:
    min_val = b
if b>max_val:
    max_val = b

#porovname s tretim cislem "c"
if b<min_val:
    min_val = c
if b>max_val:
    max_val = c
    

print("Maximum je: ", max_val)
print("Minimum je: ", min_val)