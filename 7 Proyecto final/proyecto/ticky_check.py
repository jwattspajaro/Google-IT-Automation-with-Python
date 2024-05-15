#!/usr/bin/env python3

# Importa todos los módulos de Python necesarios
import re
import sys
import operator
import csv

# Inicializa dos diccionarios:
# uno para el número de mensajes de error diferentes
# y otro para contar el número de entradas para cada usuario (dividido entre INFO y ERROR).
error = {}
per_user = {}

# Analiza cada entrada de registro en el archivo syslog.log iterando sobre el archivo.
with open("syslog.log") as f:
    for line in f:
        # Utiliza una expresión regular para extraer el nombre de usuario de cada línea.
        username = re.search(r"\((.*)\)", line).group(1)
        user_count = {'INFO': 0, 'ERROR': 0}
        if username not in per_user:
            per_user[username] = user_count
        
        # Verifica si la línea contiene un mensaje INFO y actualiza el recuento correspondiente en el diccionario per_user.
        if "INFO" in line:
            per_user[username]['INFO'] += 1

        # Si la línea contiene un mensaje ERROR, actualiza el recuento correspondiente en los diccionarios error y per_user.
        elif "ERROR" in line:
            err_msg = re.search(r"ERROR (.*) ", line).group(1)
            if err_msg not in error:
                error[err_msg] = 0
            error[err_msg] += 1
            per_user[username]['ERROR'] += 1

# Ordena el diccionario error por el número de errores de más común a menos común.
error_sorted = []
for error, count in sorted(error.items(), key=lambda item: item[1], reverse=True):
    error_sorted.append([error, count])

# Ordena el diccionario per_user por nombre de usuario.
user_sorted = []
for username in sorted(per_user.keys()):
    user_sorted.append([username, per_user[username]["INFO"], per_user[username]["ERROR"]])

# Inserta los nombres de las columnas ("Error", "Count") en la posición cero del diccionario error_sorted.
error_sorted.insert(0, ["Error", "Count"])
# Inserta los nombres de las columnas ("Username", "INFO", "ERROR") en la posición cero del diccionario user_sorted.
user_sorted.insert(0, ["Username", "INFO", "ERROR"])

# Después de ordenar estos diccionarios, guárdalos en dos archivos diferentes: error_message.csv y user_statistics.csv.
with open("error_message.csv", "w") as error_msg_file:
    writer = csv.writer(error_msg_file)
    writer.writerows(error_sorted)

with open("user_statistics.csv", "w") as user_statistics_file:
    writer = csv.writer(user_statistics_file)
    writer.writerows(user_sorted)
