diccionario = { 'a' : True, 5 : "esto es un string", 'a' : 100, 'a' : False } # Las clave deben ser inmutables

diccionario['c'] = 'nuevo string' #Crea clave/valor
diccionario['a'] = False #Si la llave/clave se encuentra, la actualiza. De lo contrario la crea

valor = diccionario['a'] #Obtiene los valores
valor = diccionario.get('a', (12,2)) #get
#valor = diccionario.get('z', (12,2))

#del diccionario[5] #del nos ayuda a eliminar

#print(diccionario)
#print(valor)

llaves = list( diccionario.keys() )#Objeto iterable
valores = tuple( diccionario.values() )

diccionario_dos = {'z' : 23, 'w' : 88}
#diccionario['z'] = diccionario_dos['z']
#diccionario['w'] = diccionario_dos['w']

diccionario.update(diccionario_dos)

print(llaves)
print(valores)
print(diccionario)
