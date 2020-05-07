from hashlib import md5
from virus_total_apis import PublicApi
import json
from termcolor import colored, cprint
import time
hora = str(time.strftime("%H:%M:%S"))

#colores
colores = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
grey, red, green, yellow, blue, magenta, cyan, white = colores
#atributos
atributos = [ ['bold'], ['dark'], ['underline'], ['blink'], ['reverse'], ['concealed'] ]
bold, dark, underline, blink, reverse, concealed = atributos
#fondos
fondos = ['on_grey','on_red','on_green','on_yellow','on_blue','on_magenta','on_cyan','on_white']
onGrey,onRed,onGreen,onYellow,onBlue,onMagenta,onCyan,onWhite = fondos
def consultarScan():
    
    response = api.get_file_report(str(md5))

    resultado = response["results"]["scans"]
    print('Resultados del scan')

    for item, valor in resultado.items():
        
        if valor['detected'] == False:
    
            print(colored('[+]', 'green')+ item +': ', colored('Limpio', 'green'))
        else:
            print(colored('[+]', 'red')+ item +': ', colored('detectado', 'red'))

    
def menu():
    cprint('\n   ██    ██ ██ ██████  ██    ██ ███████     ███████  ██████  █████  ███    ██ ', 'green')
    cprint('   ██    ██ ██ ██   ██ ██    ██ ██          ██      ██      ██   ██ ████   ██ ', 'green')
    cprint('   ██    ██ ██ ██████  ██    ██ ███████     ███████ ██      ███████ ██ ██  ██ ', 'green')
    cprint('    ██  ██  ██ ██   ██ ██    ██      ██          ██ ██      ██   ██ ██  ██ ██ ', 'green')
    cprint('     ████   ██ ██   ██  ██████  ███████     ███████  ██████ ██   ██ ██   ████ ', 'green')
    
    cprint('\n                             [+]By devkernnel', 'red')
    cprint('                             [+]github: https://github.com/kenderperez', 'red')
    cprint('                             [+]VirusTotal', 'red')
    
API_KEY = "198bde2e7a2c6675b70a6bf02b1d3504d19d2e4df5ca9df329f10e502ac4ca80"
api = PublicApi(API_KEY)
menu()
nombre_archivo = str(input(colored('\n          [+]Ingrese el nombre del archivo que desea escanear!\n          archivo: ', 'cyan')))
    
responsefile = api.scan_file(nombre_archivo)

md5 = responsefile['results']['md5']

cprint('[+]Nuestros duendecitos estan trabajando en su archivo espere por favor a que obtengan un resultado...', 'magenta')

time.sleep(200)

consultarScan()
