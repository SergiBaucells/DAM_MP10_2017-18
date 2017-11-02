num_list = []
while True:
    numero = input("Introdueix un número: ")

    if numero == "fi":
        break
    if len(numero) < 1:
        break

    try:
        numero = int(numero)
        num_list.append(numero)
    except:
        print("Ha de ser un número!!")
        continue


maxim = max(num_list)
minim = min(num_list)
print("Màxim: ", maxim)
print("Mínim: ", minim)