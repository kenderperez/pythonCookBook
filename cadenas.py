#las cadenas en python son tratadas como listas
cadena = 'hola mundo'
print(cadena[0]) #imprimira 'h'
print(cadena[0:4]) #imprime 'hola'

#Buscar una palabra dentro de una cadena

palabra = 'hola'
cadena = 'hola mundo'

print(palabra in cadena) #palabra in cadena debuelve un booleano si la palabra esta dentro de cadena devuelve True de lo contrario es False

#tambien podemos usar not in: es todo lo contrario de lo que acabamos de ver con in

print(palabra not in cadena) #si palabra no esta en cadena devuelve True, en este caso devuelve False por que 'hola' si se encuentra en 'hola mundo' 

#Convertir cadena a Mayusculas

cadena = 'hola'
cadenaEnMayusculas = cadena.upper() #el metodo .upper() convierte una cadena a mayusculas 
print(cadenaEnMayusculas)

#Convertir cadena a minusculas
cadenaEnMinusculas = cadena.lower()
print(cadenaEnMinusculas)

#Verificar si un texto esta en mayusculas o minusculas:
cadena.isupper() #False
cadena.islower() #True
cadenaEnMayusculas.isupper() #True

#evaluar si una cadena contiene solo letras 
cadena.isalpha() #devuelve un booleano en este caso True

#Evaluar si una cadena empieza o termina con una palabra espesifica
print(cadena.startswith('hola')) #True
cadena.endswith('mundo') #True
cadena.startswith('kender') #False 

#Evaluar si la primera letra es mayuscula

cadena.istitle() #false

#Metodo join() para convertir listas en cadenas:

separador = '+'
lista = ['pollo','gato','perro']
cadenaDesdeLista = separador.join(lista)
print(cadenaDesdeLista)

#Metodo split convierte cadena a lista:
cadena = 'gato perro lobo moneda peso negro'
listaDesdeCadena = cadena.split()
print(listaDesdeCadena)

#funcion el metodo find() obtiene como parametro una palabra y debuelve el indise  que esta ocupa en la cadena
buscar = 'murcielago'
cadena = 'el veloz murcielago indu comia feliz trigo y fruta'
print(cadena.find(buscar)) #9 ya que el indice de murcielago en cadena empieza en la posicion 9

#Metodo Replace:
buscar = 'microsoft'
cadena = 'microsoft es lo mejor'
reemplazo = 'linux'
nueva = cadena.replace(buscar, reemplazo)
print(nueva)
