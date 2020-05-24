from instapy_cli import client
user = 'usuario de instagram'
passw = 'clave de instagram'
text = 'texto del post'
img = 'imagen.png'


def subirImagen(texto, imagen, usuario=user, password=passw):
    
    with client(usuario, password) as cli:
        cli.upload(imagen, texto)
        
        
#para subir una imagen a instagram vasta con ejecutar la funcion subirImagen y espesificar el texto del post y el nombre de la imagen ej: imagen.png

subirImagen(text, img)
