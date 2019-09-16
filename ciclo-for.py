lista = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for valor in lista:
    pass

#nuevo_rango = range(0, 10)
nuevo_rango = range(0, 20, 4)

for valor in nuevo_rango:
    pass

for indice, valor in enumerate(lista):
    pass #print(valor, "tiene el índice", indice)

for valor in range(0, len(lista)):
    pass# print(valor)

for valor in "Curso de código facilito":
    pass# print(valor)

diccionario = {'a': 10, 'b': 20, 'c': 500}
for llave, valor in diccionario.items():
    print("La llave", llave, "tiene el valor de", valor)
