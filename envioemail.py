from email.message import EmailMessage
import smtplib

def enviar_email(email_destino,codigo):
    remitente = "lfconde@uninorte.edu.co"
    destinatario = email_destino
    mensaje = "Codigo de Confirmacion "+codigo
    email = EmailMessage()
    email["From"] = remitente
    email["To"] = destinatario
    email["Subject"] = "Codigo de Activacion "+ codigo
    email.set_content(mensaje, subtype="html")
    smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
    smtp.starttls()
    smtp.login(remitente, "amor1516")
    smtp.sendmail(remitente, destinatario, email.as_string())
    smtp.quit()