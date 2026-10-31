#importações
import smtplib
from email.message import EmailMessage
import mimetypes
import os
from dotenv import load_dotenv

class EmailManager:
    # dados de envio
    def __init__(self):
        load_dotenv()
        self.remetente = os.getenv("REMETENTE")
        self.senha = os.getenv("SENHA")
        self.msg = EmailMessage()

    # mensagem
    def enviar(self, destinatario, verificador):
        self.msg['From'] = self.remetente
        self.msg['To'] = destinatario
        self.msg['Subject'] = "Verificação de E-mail"
        self.msg.set_content(f"Aqui está seu código de verificação:\n{verificador}")

        #enviar o email

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as email:
            email.login(self.remetente, self.senha)
            email.send_message(self.msg)