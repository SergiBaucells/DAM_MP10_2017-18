def mcd(a, b):
    resto = 0
    while(b > 0):
        resto = b
        b = a % b
        a = resto
    return a



num1 = int(input("Introdueix el primer número: "))
num2 = int(input("Introdueix el segon número: "))

print("El máxim comú divisor de ", num1," y ", num2," es: ", mcd(num1, num2))