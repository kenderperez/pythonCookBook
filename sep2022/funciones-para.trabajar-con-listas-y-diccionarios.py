#Unir dos listas en una sola
lista = ['pera','manzana','mango']
lista2 = ['papaya', 'melon', 'sandia']

lista3 = lista + lista2

print(lista3)

#Cambiar el valor de un item en una lista:

lista = ['pera', 'manzana', 'fresa']
lista[1] = 'perro'
print(lista) #['pera', 'perro', 'fresa']

#Eliminar Elemento de una lista:

del lista[0]
print(lista) #['perro', 'fresa']
print(len(lista)) #2

#programa que agrega elementos a una lista

#reiniciamos la variable lista la ponemos igual a una lista vacia
lista = []
datos = ''

while True:
    datos = input('Desea agregar mas datos a la lista? deje en blanco para detener: ')
    strdatos = str(datos)
    if strdatos == '':
        break
    lista.append(strdatos)

    for i in lista:
        print(i)

#la funcion range crea una lista con los numeros del 1 al 3
lista = ['perro', 'gato', 'pollos', 'vacas']
for i in range(len(lista)):
    print('el indice: ' + str(i) + ' le pertenece el elemento: ' + lista[i])
