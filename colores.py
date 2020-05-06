#pip3 install termcolor
from termcolor import colored, cprint
#colores
colores = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
grey, red, green, yellow, blue, magenta, cyan, white = colores
#atributos
atributos = [ ['bold'], ['dark'], ['underline'], ['blink'], ['reverse'], ['concealed'] ]
bold, dark, underline, blink, reverse, concealed = atributos
#fondos
fondos = ['on_grey','on_red','on_green','on_yellow','on_blue','on_magenta','on_cyan','on_white']
onGrey,onRed,onGreen,onYellow,onBlue,onMagenta,onCyan,onWhite = fondos
#ejemplos
#cprint(string, color, fondo, attrs = atributo)
cprint('hello color', cyan)
texto = colored('Hello, World!: ', 'red')
entrada = input(texto)
cprint(entrada, red, attrs= bold)
cprint('Hello, World!', green, onRed, attrs=bold)
