def a():
    resultat = ""
    index = 0
    cadena = input("Introdueix una cadena: ")
    caracter = input("Introdueix un caràcter: ")
    if (cadena == "" or caracter == ""):
        print("La cadena/caràcter no pot estar buid!!")
    while (index < len(cadena)):
        if (len(cadena) - index == 1):
            resultat += cadena[index]
            break
        resultat += cadena[index] + caracter
        index = index + 1
    return resultat
    print(a(cadena,caracter))

def b():
    cadena = input("Introdueix una cadena: ")
    caracter = input("Introdueix un caràcter: ")
    if (cadena == "" or caracter == ""):
        print("La cadena/caràcter no pot estar buid!!")

    print(cadena.replace(' ', caracter))

def c():
    cadena = input("La seua clau és: ")
    caracter = input("Introdueix un caràcter: ")
    if (cadena == "" or caracter == ""):
        print("La cadena/caràcter no pot estar buid!!")

    cadena1 = cadena.find(str(":")) + 1
    cadena2 = cadena[cadena1:]
    print(cadena2.replace(cadena[cadena1:],caracter))

#print(a())
#print(b())
print(c())