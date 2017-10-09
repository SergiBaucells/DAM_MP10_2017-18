def invertir_numero(numero):
    return str(numero)[::-1]


num = int(input("Introdueix un número: "))

if (num == invertir_numero(num)):
    print("És palíndrom")
else:
    print("No és palíndrom")