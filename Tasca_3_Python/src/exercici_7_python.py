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
    print(a(cadena, caracter))

def b():
    cadena = input("Introdueix una cadena: ")
    caracter = input("Introdueix un caràcter: ")
    if (cadena == "" or caracter == ""):
        print("La cadena/caràcter no pot estar buid!!")

    print(cadena.replace(' ', caracter))

def c():
    cadena = input("La seua clau és: ")
    caracter = input("Introdueix un caràcter: ")
    if (cadena == ""):
        print("La cadena/caràcter no pot estar buid!!")

    index = 0
    while index < len(cadena):
        lletra = cadena[index]
        if lletra == str(int(lletra)):
            lletra = caracter
        index = index + 1



#print(a())
#print(b())
print(c())