def a():
    cadena = input("Introdueix una cadena: ")
    cadena2 = input("Introdueix una altra cadena: ")

    if cadena.find(cadena2) > -1:
        print(cadena2, "és una subcadena de", cadena)
    else:
        print(cadena2 ,"no és una subcadena de", cadena)

def b():
    cadena = input("Introdueix una cadena: ")
    cadena2 = input("Introdueix una altra cadena: ")
    if cadena < cadena2:
        print(cadena)
    else:
        print(cadena2)

print(a())
print(b())
