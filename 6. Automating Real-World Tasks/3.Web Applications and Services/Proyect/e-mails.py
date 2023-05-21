import email.message
import mimetypes
import os.path
import smtplib

def generate(sender, recipient, subject, body, attachment_path):
  """Crea un correo electrónico con un archivo adjunto."""
  
  # Formato básico del correo electrónico
  message = email.message.EmailMessage()
  message["From"] = sender
  message["To"] = recipient
  message["Subject"] = subject
  message.set_content(body)

  # Procesa el archivo adjunto y lo agrega al correo electrónico
  attachment_filename = os.path.basename(attachment_path)
  
  # Adivina el tipo de MIME del archivo adjunto
  mime_type, _ = mimetypes.guess_type(attachment_path)
  mime_type, mime_subtype = mime_type.split('/', 1)

  # Abre el archivo en modo binario, lee los datos y añade el archivo al mensaje
  with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(),
                          maintype=mime_type,
                          subtype=mime_subtype,
                          filename=attachment_filename)

  return message

def send(message):
  """Envía el mensaje al servidor SMTP configurado."""
  
  # Se conecta al servidor SMTP
  mail_server = smtplib.SMTP('localhost')
  
  # Envía el mensaje
  mail_server.send_message(message)
  
  # Cierra la conexión con el servidor SMTP
  mail_server.quit()
