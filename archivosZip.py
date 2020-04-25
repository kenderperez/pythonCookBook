#! python3
import zipfile

#CREAR ARCHIVO ZIP

archivoZip = zipfile.ZipFile('nuevo.zip','w') #abre un nuevo archivo zip con  permisos de escritura --mirar: segundo parametro
archivoZip.write('documento.txt', compress_type=zipfile.ZIP_DEFLATED) #este archivo es el que se comprimira y ya tiene que estar en la carpeta raiz del programa
archivoZip.close()

#OPERACIONES DE LECTURA ZIP

archivoZip = zipfile.ZipFile('archivo.zip') #para abrir un archivo zip
contenido = archivoZip.namelist() #guarda el contenido del archivo zip en una lista o array
archivoZip.extractall() #para extraer todo el contenido de un archivo zip
archivoZip.extract(contenido[0]) #para extraer un solo archivo
archivoZip.close()
