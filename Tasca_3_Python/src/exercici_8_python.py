def a():
    cadena = input("Introdueix una cadena: ")
    vocals = "a", "e", "i", "o", "u"
    cadena2 = ""
    if (cadena == ""):
        print("La cadena no pot estar buida!!")
    for lletra in cadena:
        if not (lletra.lower() in vocals):
            cadena2 += lletra
    print(cadena2)

def b():
    cadena = input("Introdueix una cadena: ")
    consonants = ("BCDFGHJKLMNÑPQRSTVWXYZbcdfghjklmnñpqrstvwxyz")
    if (cadena == ""):
        print("La cadena no pot estar buida!!")
    for lletra in consonants:
        cadena = cadena.replace(lletra,"")
    print(cadena)

def d():
    cadena = input("Introdueix una cadena: ")
    cadena2 = ""
    if (cadena == ""):
        print("La cadena no pot estar buida!!")
    for caracter in cadena:
        if caracter != " ":
            cadena2 = cadena2 + caracter
    if cadena2.lower() == cadena2[::-1].lower():
        print("Es palindrom")
    else:
        print("No es palindrom")

print(a())
print(b())
#print(c()) #No el vaig saber fer!
print(d())