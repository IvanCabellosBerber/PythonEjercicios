numero = int(input("Numero a introducir"))
total = 0
if ((int(numero) % 2 == 0)):
    print("Es par")

    for x in range(numero):
        numero = numero + 2
        total = total + int(numero)
    print(total)

else:
    print("Es impar")
    for x in range(numero):
        numero = numero + 2
        total = total + int(numero)

    print(total)