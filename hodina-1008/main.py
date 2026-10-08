#souradnice panacka
x_panacka=int(input("Zadejte x: "))
y_panacka=int(input("Zadejte y: "))

#nebezpečná plocha
x1 = 2
x2 = 6
y1 = 2
y2 = 5

#test, zda došlo ke kolizi
if x_panacka >=x1 and x_panacka <= x2 and y_panacka>=y1 and y_panacka <=y2 :
    print("Došlo ke kolizi!")

else:print("Vedle trubko!")