import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def email():
    message = MIMEMultipart()

    emailSend = input('Informe seu email (aceitamos apenas gmail e hotmail): ')
    message['From'] = emailSend

    pinword = input('Informe sua senha: ')
    password = pinword

    emailReceive = input('Informe o email destinatário: ')
    message['To'] = emailReceive

    message['Subject'] = "Email automático enviado com sucesso!"

    body = "Olá! Você recebeu um email de teste do Batley"
    message.attach(MIMEText(body, 'plain'))

    if "gmail.com" not in emailSend:
        smtpSend = 'smtp.live.com'
    else: 
        smtpSend = 'smtp.gmail.com'

    smtp = smtplib.SMTP(smtpSend, port=587)
    smtp.starttls()
    smtp.login(message['From'], password)
    smtp.sendmail(message['From'], message['To'], message.as_string())
    smtp.quit()

if __name__ == "__main__":
    email()
    print("Enviado com sucesso!")