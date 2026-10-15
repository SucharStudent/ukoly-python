#vypis promennych
a = int(input("Zadejte číslo A: "))
b = int(input("Zadejte číslo B: "))
c = int(input("Zadejte číslo C: "))

odklad= 0

#porovnani a prohozeni a, b 
if a > b:
    odklad = a
    a = b
    b = odklad

#porovnani a prohození b, c
if b > c:
    odklad = b
    b = c
    c = odklad

#porovnani a prohození a, b
if a > b:
    odklad = a
    a = b
    b = odklad

print(a, b, c)