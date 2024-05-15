#!/usr/bin/env python3
# Código de Coursera

import datetime
import email
import smtplib
import sys

def usage():
    print("send_reminders: Enviar recordatorios de reuniones")
    print()
    print("invocación:")
    print("    send_reminders 'date|Meeting|Emails' ")
    return 1

def dow(date):
    # Convierte la fecha en el día de la semana correspondiente
    dateobj = datetime.datetime.strptime(date, r"%Y-%m-%d")
    return dateobj.strftime("%A")

def message_template(date, title):
    # Crea la plantilla del mensaje de correo electrónico con la fecha y el título de la reunión
    message = email.message.EmailMessage()
    weekday = dow(date)
    message['Subject'] = f'Recordatorio de reunión: "{title}"'
    message.set_content(f'''
Hola a todos!
    
Este es un correo rápido para recordarles que tenemos una reunión sobre: "{title}""
el {weekday} {date}

¡Nos vemos allí!
''')
    return message

def send_message(message, emails):
    # Envía el mensaje a las direcciones de correo electrónico proporcionadas
    smtp = smtplib.SMTP('localhost')
    message['From'] = 'noreply@example.com'
    for email in emails.split(','):
        del message['To']
        message['To'] = email
        smtp.send_message(message)
    smtp.quit()

def main():
    if len(sys.argv) < 2:
        return usage()

    try:
        # Extrae la fecha, hora y correos electrónicos de los argumentos de la línea de comandos
        date, time, emails = sys.argv[1].split('|')
        # Crea el mensaje de correo electrónico utilizando la plantilla
        message = message_template(date, time)
        # Envía el mensaje a las direcciones de correo electrónico proporcionadas
        send_message(message, emails)
        print("Recordatorios enviados correctamente a:", emails)
    except Exception as e:
        # Captura cualquier excepción y la imprime
        print("Error al enviar el correo electrónico:", e, file=sys.stderr)

if __name__ == '__main__':
    # Ejecuta la función main y sal del script con el código de salida adecuado
    sys.exit(main())
