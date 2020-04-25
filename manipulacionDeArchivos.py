"""
7.2. Manipulación de archivos

Para escribir o leer cadenas de caracteres para/desde archivos (otros tipos deben ser convertidas a cadenas de caracteres). Para esto Python incorpora un tipo integrado llamado file, el cual es manipulado mediante un objeto archivo el cual fue generado a través de una función integrada en Python, a continuación se describen los procesos típicos y sus referencias a funciones propias del lenguaje:
7.2.1. Abrir archivo

La forma preferida para abrir un archivo es usando la función integrada open().
7.2.2. Leer archivo

La forma preferida para leer un archivo es usando algunas de los métodos del tipo objeto file como read(), readline() y readlines().
7.2.3. Escribir archivo

La forma preferida para escribir un archivo es usando el método del tipo objeto file llamado write().
7.2.4. Cerrar archivo

La forma preferida para cerrar un archivo es usando el método del tipo objeto file llamado close().
7.2.5. Archivos con modulo os

El módulo os de Python le permite a usted realizar operaciones dependiente del Sistema Operativo como crear una carpeta, listar contenidos de una carpeta, conocer acerca de un proceso, finalizar un proceso, etc. Este módulo tiene métodos para ver variables de entornos del Sistema Operativo con las cuales Python esta trabajando en mucho más. Aquí la documentación Python para el módulo os.

A continuación algunos útiles métodos del módulo os que pueden ayudar a manipular archivos y carpeta en su programa Python:

Crear una nueva carpeta """

import os
os.makedirs("Ana_Poleo")

#Listar el contenidos de una carpeta

os.listdir("./")

#Mostrar el actual directorio de trabajo

directorioActual = os.getcwd()
print(directorioActual)

#Mostrar el tamaño del archivo en bytes del archivo pasado en parámetro

consulta = os.path.getsize("Ana_Poleo")
print(consulta)

#¿Es un archivo el parámetro pasado?

consulta = os.path.isfile("Ana_Poleo")
print(consulta)


#¿Es una carpeta el parámetro pasado?


consulta = os.path.isdir("Ana_Poleo")
print(consulta)
#True

#Cambiar directorio/carpeta

os.chdir("Ana_Poleo")
directorioActual = os.getcwd()
#'/home/usuario/python/Ana_Poleo'
print(os.listdir("./"))
#[]
os.chdir("../")
print(directorioActual)
#'/home/usuario/python'

#Renombrar un archivo

os.rename("Ana_Poleo","Ana_Carolina")
print(os.listdir("./"))
#['Ana_Carolina']

#Eliminar un archivo

os.chdir("Ana_Carolina")
archivo = open(os.getcwd()+'/datos.txt', 'w')
archivo.write("Se Feliz!")
archivo.close()
os.getcwd()
#'/home/usuario/python/Ana_Carolina'
print(os.listdir("./"))
#['datos.txt']
os.remove(os.getcwd()+"/datos.txt")
print(os.listdir("./"))
#[]

#Eliminar una carpeta

os.rmdir("Ana_Carolina")
os.chdir("Ana_Carolina")
"""Traceback (most recent call last):
File "<stdin>", line 1, in <module>
OSError: [Errno 2] No such file or directory: 'Ana_Carolina'

Lanza una excepción OSError cuando intenta acceder al directorio que previamente elimino y este no encuentra.
7.2.6. Ejemplos de archivos"""

"""A continuación, se presentan algunos ejemplos del uso del tipo objeto file:

Ejemplo de iterar un archivo para leerlo

Usted puede iterar sobre un archivo como se muestra a continuación:"""

archivo = open('datos.txt', 'r')
for linea in archivo:
print(linea)
#Este es una prueba

#y otra prueba
archivo.close()

#Ejemplo de iterar un archivo con escritura y lectura

#Usted puede manipular un archivo con permisos de escritura y lectura, ademas de interactuar de el mismo como se muestra a continuación:


print("\nCrear un archivo")
print("================")

NOMBRE_ARCHIVO = 'datos.txt'

archivo = open(NOMBRE_ARCHIVO, 'w') # abre el archivo datos.txt
archivo.write('Este es una prueba \ny otra prueba.')
archivo.close()

if NOMBRE_ARCHIVO in os.listdir("."):
print("\nArchivo creado en la ruta: \n\n\t{0}/{1}".format(os.getcwd(), NOMBRE_ARCHIVO))
else:
print("El archivo no fue creado!!!\n")


print("\n\nLeer un archivo")
print("===============\n")

archivo = open(NOMBRE_ARCHIVO, 'r')
contenido = archivo.read()
print(contenido)
archivo.close()


print("\n\nIterar sobre un archivo")
print("=======================\n")

archivo = open(NOMBRE_ARCHIVO, 'r')
for linea in archivo:
print(linea)
print("\n")
archivo.close()


print("\nEliminar un archivo")
print("===================")

os.remove(os.getcwd()+"/"+NOMBRE_ARCHIVO)
print("\nEliminado archivo desde la ruta: \n\n\t{0}/{1}".format(os.getcwd(), NOMBRE_ARCHIVO))

#7.2.7. Ayuda integrada

#Usted puede consultar toda la documentación disponible sobre los tipos objeto file desde la consola interactiva de la siguiente forma:

help(file)

#Para salir de esa ayuda presione la tecla q.

