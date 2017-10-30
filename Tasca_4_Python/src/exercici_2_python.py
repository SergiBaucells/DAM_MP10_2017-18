def centre(llista):
    segona_llista = llista.copy()
    try:
        del segona_llista[:1]
        segona_llista.pop()
    except:
        print("Ha de ser una llista i/o no pot ser buida!!")
    return segona_llista

llista = [1, 2, 3, 4]
print(llista)
print(centre(llista))