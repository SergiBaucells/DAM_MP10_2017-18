
numero = 0
suma = 0
comptador = 0
menor = None
major = None

while True:
    try:
        numero = input("Introdueix un número: ")
        numero = int(numero)
        if major is None or numero > major :
            major = numero
        if menor is None or numero < menor :
            menor = numero
        suma = numero+suma
        comptador = comptador + 1
    except:
        if numero == "fi":
            break
        print("El valor introduït ha de ser un número enter!")

print("\nSuma números: " + str(suma) + "\nTotal de números introduits: " + str(comptador) + "\nMajor: " + str(major) + "\nMenor: " + str(menor))
