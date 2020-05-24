from instapy_cli import client
user = 'usuario de instagram'
passw = 'clave de instagram'
text = 'texto del post'
img = 'ruta de la imagen'


def subirImagen(usuario, password, texto, imagen):
    
    with client(usuario, password) as cli:
        cli.upload(imagen, texto)
        
        
#para subir una imagen a instagram vasta con poner

subirImagen(user, passw, text, img)
