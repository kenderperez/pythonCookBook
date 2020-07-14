#IMPORTANTE: codificar el script en UTF-8 para poder utilizar vocales acentuadas, etc, ...
import smtplib, getpass, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64

print("**** Enviar email con Gmail ****")
user = input("Cuenta de gmail: ")
password = getpass.getpass("Password: ")

#Para las cabeceras del email
remitente = input("From, ejemplo: administrador <admin@gmail.com>: ")
destinatario = input("To, ejemplo: amigo <amigo@mail.com>: ")
asunto = input("Subject, Asunto del mensaje: ")
mensaje = input("Mensaje HTML: ")
archivo = input("Adjuntar archivo: ")

#Host y puerto SMTP de Gmail
gmail = smtplib.SMTP('smtp.gmail.com', 587)

#protocolo de cifrado de datos utilizado por gmail
gmail.starttls()

#Credenciales
gmail.login(user, password)

#muestra la depuración de la operacion de envío 1=true
gmail.set_debuglevel(1)

header = MIMEMultipart()
header['Subject'] = asunto
header['From'] = remitente
header['To'] = destinatario

mensaje = MIMEText(mensaje, 'html') #Content-type:text/html
header.attach(mensaje)

if (os.path.isfile(archivo)):
 adjunto = MIMEBase('application', 'octet-stream')
 adjunto.set_payload(open(archivo, "rb").read())
 encode_base64(adjunto)
 adjunto.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(archivo))
 header.attach(adjunto)

#Enviar email
gmail.sendmail(remitente, destinatario, header.as_string())

#Cerrar la conexión SMTP
gmail.quit()
