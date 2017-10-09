def invertir_numero(numero):
    return str(numero)[::-1]

while True:
    try:
        num = int(input("Introdueix un número: "))     
        print("Número Invertit: " + invertir_numero(num))
        break
    except:
        print("El valor introduït ha de ser un número enter")