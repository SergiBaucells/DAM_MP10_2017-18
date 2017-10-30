def retalla(llista):
    try:
        del llista[:1]
        llista.pop()
    except:
        print("Ha de ser una llista i/o no pot ser buida!!")
    return None

llista = [1, 2, 3, 4]
print(retalla(llista))
print(llista)