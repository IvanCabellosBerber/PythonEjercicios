print("Adivina la clave secreta, tienes 3 intentos")
clave = str(input("Dime la clave"))

num_intentos = 3


while num_intentos != -1:
    if num_intentos == 0:
        raise Exception("Estas fuera!")
    if num_intentos <= 3:
        if clave == "eureka":
            print("Eres el puto amo, se ha abierto (y la caja tambien)")
        else:
            num_intentos -= 1
            print("Eres retrasado, sigue cerrada, y las piernas tambien, te quedan ", num_intentos, " intentos")
            str(input("Introduce otra vez la clave"))
