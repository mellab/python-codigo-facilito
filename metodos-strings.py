course = 'Curso'
my_string = 'Código Facilito!'

""" Formato """ # Alternativa para comentarios
result = '{a} de {b}'.format(a = course, b = my_string)
result = result.lower() #Curso de Código Facilito!
#result = result.upper()
#result = result.title()

""" Búsqueda """

pos = result.find('código')
count = result.count('c')

#print(pos)
#print(result[9])

new_string = result.replace('c', 'x')
new_string = result.split(' ')

#print(count)
print(new_string)
