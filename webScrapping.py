  #! python3
from bs4 import BeautifulSoup
import requests


url = 'https://resultados.as.com/resultados/futbol/primera/clasificacion'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser') #contenido html de la web
elementosSoup = soup.find_all('span', class_='nombre-equipo') #buscar elementos span con la clase nombre-equipo

for iten in elementosSoup:
	print(iten.text)

