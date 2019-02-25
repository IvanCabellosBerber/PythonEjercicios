nin = int(input("Dime cuantos niños"))
nina = int(input("Dime cuantas niñas"))

total = nin + nina

perc_nin = (nin * 100) / total
perc_nina = 100 - perc_nin

print(str(perc_nin) + "% de niños y, " + str(perc_nina) + "% de niñas")

