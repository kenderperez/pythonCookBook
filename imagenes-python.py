#pip install pillow
from PIL import Image, ImageFont, ImageDraw
import os

ancho = 900
alto = 900
color = 'purple'
img = Image.new('RGBA', (ancho, alto), color)
texto = 'hello world'

fuente = ImageFont.truetype('arial.ttf', 75)
w,h = fuente.getsize(texto)

x = 100
y = 100
draw = ImageDraw.Draw(img)

draw.text((x, y), texto, font=fuente, fill='black')

img.show()
img.save('imagen.png')
