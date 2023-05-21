import emails
import os
import reports

# Creamos los datos de la tabla
table_data=[
  ['Nombre', 'Cantidad', 'Valor'],
  ['elderberries', 10, 0.45],
  ['figs', 5, 3],
  ['apples', 4, 2.75],
  ['durians', 1, 25],
  ['bananas', 5, 1.99],
  ['cherries', 23, 5.80],
  ['grapes', 13, 2.48],
  ['kiwi', 4, 0.49]]

# Generamos el informe con los datos de la tabla
reports.generate("/tmp/report.pdf", "Inventario completo de mis frutas", "Estas son todas mis frutas.", table_data)

# Definimos el remitente y el destinatario del correo electrónico
sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))

# Definimos el asunto y el cuerpo del correo electrónico
subject = "Lista de frutas"
body = "Hola\n\nTe envío en adjunto la lista de todas mis frutas."

# Generamos el correo electrónico con el informe adjunto
message = emails.generate(sender, receiver, subject, body, "/tmp/report.pdf")

# Enviamos el correo electrónico
emails.send(message)
