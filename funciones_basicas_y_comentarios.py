#esto es un comentario de una sola linea
"""esto es un comentarios
multilinia en python"""
"""aca se ven los tipos de datos y algunas funciones basicas los comentarios y el bucle for"""
#esta es una variable en python
persona = 'kender'

#esta funcion imprime por consola
print('hola mundo')

#la interpolacion de strings en python se hace de la siguiente manera

print(f'hola {persona}')

#la funcion type devuelve el tipo de dato que le pasamos como parametro ejemplo:

print(type(persona))  #string
print(type(True))     #booleano
print(type(5))        #int
print(type(["Saab", "Volvo", "BMW"]))  #list o array
print(type({'nombre': 'kender', 'profecion': 'programador'}))  #diccionario o objeto
print(type(("Saab", "Volvo", "BMW")))  #tupla


carros = ["Saab", "Volvo", "BMW"]
#condicional if
if 'Volvo' in carros:
    print('true')
else:
    print('false')
#bucle for
for carro in carros:
    print(carro)
