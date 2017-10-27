def cadena_a():
    index = 0
    cadena = input("Introdueix una cadena: ")
    if (cadena == ""):
        print("La cadena no pot estar buida!!")
    while index < len(cadena):
        lletra = cadena[index]
        index = index + 1
        if index == 0 or index % 2:
            print (lletra)

def cadena_b():
    cadena = input("Introdueix una cadena: ")
    index = 0
    invertida = ""
    j = len(cadena)-1
    
    if (cadena == ""):
        print("La cadena no pot estar buida!!")
    else:
        while (index <= j):
            invertida = invertida + cadena[j]
            j = j - 1
        print(cadena, invertida, sep="")

print(cadena_a())
print(cadena_b())