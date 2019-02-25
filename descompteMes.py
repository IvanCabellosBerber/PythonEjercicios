mes = str(input("Dime a que mes estamos").upper())
importe = int(input("Dime cuanto tienes que pagar"))

if (mes == "OCTUBRE"):
    importe = importe * 0.85
    print("Tienes que pagar " + str(importe))

else:
    print("No tienes descuento, se queda en: " + str(importe))