contador = 0
bandera = True

while bandera:
    print(contador)
    contador += 1 #Aumentar en 1 el contador

    if contador == 5:
        continue

    if contador == 6:
        bandera = False #break

else:
    print('El while ha terminado')
