import requests
from bs4 import BeautifulSoup
import re
import time

patron = re.compile('\[[0-9]+]')
def buscarEnWiki(palabra):
    page = requests.get('https://es.wikipedia.org/wiki/' + palabra)
    soup = BeautifulSoup(page.content, 'html.parser') #contenido html de la web
    elemento = soup.find_all('p')
    cont1 = elemento[0].text
    cont2 = elemento[1].text
    cont = cont1 + '\n' + cont2
    regular = patron.findall(cont)
    for item in regular:
        buscar = str(item)
        cadena = cont
        reemplazo = ''
        cont = cadena.replace(buscar, reemplazo)
	
    return cont
print('          __      __.__ __   .__                  .___.__        ')
print('         /  \    /  \__|  | _|__|_____   ____   __| _/|__|____   ')
print('         \   \/\/   /  |  |/ /  \____ \_/ __ \ / __ | |  \__  \  ')
print('          \        /|  |    <|  |  |_> >  ___// /_/ | |  |/ __ \_')
print('           \__/\  / |__|__|_ \__|   __/ \___  >____ | |__(____  /')
print('                \/          \/  |__|        \/     \/         \/ ')
while True:
    dato = str(input('            [+] Ingresa una palabra para buscarla en Wikipedia!\n            [+] Busqueda: '))
    dato1 = dato.replace(' ', '_')

    if dato == '!q':
        break
    busqueda = buscarEnWiki(str(dato1))
    file = open(dato+'.txt', 'w')
    file.write(busqueda)
    file.close()
    print('Resultado de la busqueda para ' + dato.upper() + ':\n')
    print(busqueda)
    print('            [-] Escriba !q para salir')

  




