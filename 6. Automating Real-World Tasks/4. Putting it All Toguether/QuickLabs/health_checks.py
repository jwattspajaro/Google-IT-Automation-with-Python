#!/usr/bin/env python3

import os
import shutil
import psutil
import socket
import smtplib
from email.message import EmailMessage
import time

def generate_email(sender, receiver, subject, body):
    """Genera un objeto EmailMessage con los datos especificados"""
    message = EmailMessage()
    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = subject
    message.set_content(body)
    return message

def send_email(message):
    """Envía un email utilizando un servidor SMTP local"""
    with smtplib.SMTP('localhost') as mail_server:
        mail_server.send_message(message)

def check_cpu_usage():
    """Verifica el uso de CPU y devuelve True si es inferior al 80%"""
    usage = psutil.cpu_percent(1)
    return usage < 80

def check_disk_usage():
    """Verifica el espacio libre en disco y devuelve True si es superior al 20%"""
    du = shutil.disk_usage("/")
    free_percent = du.free / du.total * 100
    return free_percent > 20

def check_available_memory():
    """Verifica la memoria disponible y devuelve True si es superior a 500MB"""
    available_memory = psutil.virtual_memory().available / (1024 * 1024)
    return available_memory > 500

def check_localhost():
    """Verifica si "localhost" se resuelve a "127.0.0.1" y devuelve True si es así"""
    localhost = socket.gethostbyname('localhost')
    return localhost == '127.0.0.1'

def main():
    # Configuración de correo electrónico
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))

    # Verificar las condiciones
    conditions = {
        check_cpu_usage: "CPU usage is over 80%",
        check_disk_usage: "Available disk space is less than 20%",
        check_available_memory: "Available memory is less than 500MB",
        check_localhost: "localhost cannot be resolved to 127.0.0.1"
    }

    while True:
        error = False
        error_message = ""

        for condition, message in conditions.items():
            if not condition():
                error = True
                error_message += "- {}\n".format(message)

        if error:
            # Enviar correo electrónico de error
            subject = "Error - Health Check"
            body = "Please check your system and resolve the following issues:\n\n" + error_message
            email_message = generate_email(sender, receiver, subject, body)
            send_email(email_message)

        # Esperar 60 segundos antes de la siguiente verificación
        time.sleep(60)

if __name__ == "__main__":
    main()
