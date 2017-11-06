#append() Agrega un artícle al final de la llista
llista = ['Python','es']
llista.append('guay!')
print(llista)

#clear() Elimina tots els elements de la llista
llista = ['Python','es','guay!']
llista.clear()
print(llista)

#copy() Retorna una copia de la llista
llista = ['Python','es','guay!']
llista2 = llista.copy()
print(llista)
print(llista2)

#count() Retorna la cantitat de vegades que apareix X a la llista
llista = ['Python','es','guay!','Python','es','easy!']
print(llista.count('Python'))

#extend() Amplia la llista agregant tots els elements del iterable
llista = ['Python','es','guay!']
llista.extend(llista)
print(llista)

#index() Retorna un index
llista = ['Python','es','guay!']
print(llista)
print(llista.index('guay!'))

#insert() Agrega un artícle a una posició determinada
llista = ['Python','es','guay!']
llista.insert(3,'jeje!')
print(llista)

#pop() Extrau l'article d'una posició determinada de la llista i el retorna
llista = ['Python','es','guay!']
print(llista.pop(1))
print(llista)

#remove() Elimina el primer element de la llista on el seu valor sigui X
llista = ['Python','es','guay!']
llista.remove('Python')
print(llista)

#reverse() Retorna una llista al revés
llista = ['Python','es','guay!']
llista.reverse()
print(llista)

#sort() Ordena els element d'una llista
llista = [5,1,2,4,3]
llista.sort()
print(llista)