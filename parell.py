numero = int(input("Numero a comprobar"))

while (numero != "salir"):
    if (numero == 0):
        print("Es 0, no eso no vale")
        numero = int(input("Introduce de nuevo"))
    elif ((numero / 2) != 0):
        print(str(numero) + " es impar")
        numero = int(input("Introduce de nuevo"))
    else:
        print(str(numero) + " es par")
        numero = int(input("Introduce de nuevo"))