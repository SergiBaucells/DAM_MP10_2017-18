
numero = 0
suma = 0
comptador = 0
mitjana = 0

while True:
    try:
        numero = input("Introdueix un número: ")
        numero = int(numero)
        suma = numero+suma
        comptador = comptador + 1
    except:
        mitjana = suma/comptador
        if numero == "fi":
            break
        print("El valor introduït ha de ser un número enter!")

print("\nSuma números: " + str(suma) + "\nTotal de números introduits: " + str(comptador) + "\nMitjana: " + str(mitjana))
