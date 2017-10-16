n, cont = 4, 2
num = int(input("Introdueix un número: "))
if(num > 2):
    cad = "2 - 3"
    while cont < num:
        i = 2
        while i <= n:
            if(i == n):
                cad = cad + " - " + str(i)
                cont = cont + 1
            else:
                if(n % i == 0):
                    i = n
            i = i + 1
        n = n + 1
    print(cad)
else:
    if(num > 0):
        if(num == 1):
            print("Es primer 2")
        else:
            print("Es primer 2, 3")
    else:
        print("Introdueix un número positiu!")