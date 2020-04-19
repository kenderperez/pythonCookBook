#!/usr/bin/env python
lista = ["Saab", "Volvo", "BMW"]  #list o array
diccionario = {'nombre': 'kender', 'profecion': 'programador'}  #diccionario o objeto
tupla = ("Saab", "Volvo", "BMW") #tupla
string = 'esto es una cadena de texto' #string

#convercion de datos
listaDesdeString = list(string) #la funcion list convierte lo que se le pase como parametro en una lista
print(listaDesdeString)
stringDesdeLista = ''.join(listaDesdeString) #la funcion join convierte lo que se le pasa como parametro en un string
print(stringDesdeLista)
palabra = 'mundo'
print(f'hola{palabra}') #las interpolaciones de string solo se pueden usar de python 3 en adelante



