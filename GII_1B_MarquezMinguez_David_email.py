
"""
*******************************************************************************
* Nombre: gmail.py                                                            *
* OBJ: enviar un email.                                                       *
* Autor: David Marquez Minguez                                                *
* Referencias: www.youtube.com/watch?v=KfDJOgqR4VU                            *
*******************************************************************************
"""

def envio_gmail():

    """ Nada -> Nada
    OBJJ: Enviar un email.
    PRE: Las cuentas deben existir. """

    # Cabeceras del email.

    emisor = 'From, usuario '
    receptor = input('To, Introduce gmail del receptor(receptor@gmail.com): ')
    asunto = 'GII_1B_MarquezMinguez_David_email '
    archivo = input('Adjuntar archivo: ')

    #Importamos cabeceras.

    import smtplib, getpass, os #getpass: entrada de datos, no visible en consola .
    from email.mime.multipart import MIMEMultipart 
    from email.mime.text import MIMEText #Mensaje tip HTML

    #Funciones necesarias para poder adjuntar el archivo 

    from email.mime.base import MIMEBase
    from email.encoders import encode_base64

    # Pedimos los datos al usuario.

    usuario = input('Introduce tu cuenta de gmail: ')
    contrasenia = getpass.getpass('Introduce la contrasenia: ')#Aunque el programa funciona, salta un error en el getpass

    #Host y puerto SMTP de gmail.

    gmail = smtplib.SMTP('smtp.gmail.com', 587)

    #Protocolo de cifrado de datos.

    gmail.starttls()

    #Creenciales del usuario.

    gmail.login(usuario, contrasenia)

    #Mostramos la depuracion mientras se envia el mensaje.

    cabecera = MIMEMultipart()
    cabecera['Subject'] = asunto
    cabecera['From'] = emisor
    cabecera['To'] = receptor

    #Preparamos el el mensaje del email.

    if (os.path.isfile(archivo)): #Comprobamos si el archivo existe.

        adjunto = MIMEBase('application', 'octet-stream')
        adjunto.set_payload(open(archivo, 'rb').read())
        encode_base64(adjunto) #Convertir archivo en base 64.
        adjunto.add_header('Content-Dissposition', 'attachment; filename= %s ' %os.path.basename(archivo))
        cabecera.attach(adjunto)

    #Enviar email.

    gmail.sendmail(emisor, receptor, cabecera.as_string())

    #Cerramos conexion SMTP.

    gmail.quit()

#Probador
'''
# Cabeceras del email.

emisor = 'From, usuario '
receptor = input('To, Introduce gmail del receptor(receptor@gmail.com): ')
asunto = 'Subject, GII_1B_MarquezMinguez_David_email '
archivo = input('Adjuntar archivo: ')'''
envio_gmail()
    
