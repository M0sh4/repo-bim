import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from report import generate

# Configuración del correo
SMTP_SERVER = "smtp.gmail.com"  # Cambia esto si usas otro proveedor (ejemplo: Outlook: smtp.office365.com)
SMTP_PORT = 587  # Usar 465 para SSL o 587 para TLS
EMAIL_USER = "enviocorreosdr@gmail.com"  # Reemplázalo con tu correo
EMAIL_PASSWORD = ""  # Tu contraseña de aplicación

# Configuración del correo electrónico
def enviar(destinatario, asunto, cc):
    try:
        # Crear mensaje
        mensaje = MIMEMultipart()
        mensaje["From"] = EMAIL_USER
        mensaje["To"] = destinatario
        mensaje['CC'] = ",".join(cc)
        mensaje["Subject"] = asunto
        mensaje.attach(MIMEText(generate(), "html"))  # "plain" para texto simple; usa "html" para HTML
        # Conexión con el servidor SMTP
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as servidor:
            servidor.starttls()  # Iniciar conexión segura TLS
            servidor.login(EMAIL_USER, EMAIL_PASSWORD)  # Autenticarse
            servidor.sendmail(EMAIL_USER, [destinatario] + cc, mensaje.as_string())  # Enviar correo
            print(f"Correo enviado exitosamente a {destinatario}")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
def enviarCorreoTimeOut(destinatario, asunto, cc):
    try:
        # Crear mensaje
        mensaje = MIMEMultipart()
        mensaje["From"] = EMAIL_USER
        mensaje["To"] = destinatario
        mensaje['CC'] = ",".join(cc)
        mensaje["Subject"] = asunto
        mensaje['Description']
        mensaje.attach(MIMEText("SE MURIO EL TOKEN DE AGENTES Y ADMINS. \n TIMEDDDDDDDD OUTTTTTTTTTTTTT", "plain"))  # "plain" para texto simple; usa "html" para HTML
        # Conexión con el servidor SMTP
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as servidor:
            servidor.starttls()  # Iniciar conexión segura TLS
            servidor.login(EMAIL_USER, EMAIL_PASSWORD)  # Autenticarse
            servidor.sendmail(EMAIL_USER, [destinatario] + cc, mensaje.as_string())  # Enviar correo
            print(f"Correo enviado exitosamente a {destinatario}")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
