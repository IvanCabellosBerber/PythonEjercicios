num = int(input("Dime un numero"))
lista_num = []

while num != -1:
    lista_num.append(num)
    num = int(input("Dime otro numero"))

total = 0
for x in lista_num:
    total = total + x

print(total)
