def invertit_cadena():
    cadena = input("Introdueix una cadena: ")
    index=0
    invertida=""
    j=len(cadena)-1

    if (cadena == ""):
        print("La cadena no pot estar buida!!")
    else:
        while (index <= j):
            invertida = invertida + cadena[j]
            j = j - 1
        print("Paraula invertida: ", invertida)

print(invertit_cadena())
