#!/usr/bin/env python3

import re
import sys
import operator
import csv

# Inicializar dos diccionarios:
# uno para el número de mensajes de error diferentes
# y otro para contar el número de entradas para cada usuario (dividido entre INFO y ERROR).
error = {}
per_user = {}

# Recorrer cada entrada de registro en el archivo syslog.log iterando sobre el archivo.
with open("syslog.log") as f:
    for line in f:
        username = re.search(r"\((.*)\)", line).group(1)
        user_count = {'INFO': 0, 'ERROR': 0}
        if username not in per_user:
            per_user[username] = user_count
        # Para cada entrada de registro, primero se verifica si coincide con los formatos de mensaje INFO o ERROR. Se deben utilizar expresiones regulares para esto.
        # Cuando se obtiene una coincidencia exitosa, se agrega uno al valor correspondiente en el diccionario per_user.
        if "INFO" in line:
            per_user[username]['INFO'] += 1

        # Si se obtiene un mensaje de ERROR, se agrega uno a la entrada correspondiente en el diccionario error utilizando la estructura de datos adecuada.
        elif "ERROR" in line:
            err_msg = re.search(r"ERROR (.*) ", line).group(1)
            if err_msg not in error:
                error[err_msg] = 0
            error[err_msg] += 1
            per_user[username]['ERROR'] += 1

# Después de procesar las entradas de registro del archivo syslog.log, es necesario ordenar tanto el diccionario per_user como el diccionario error antes de crear los archivos de informe CSV.
error_sorted = []
user_sorted = []

# El diccionario error se debe ordenar por el número de errores de mayor a menor.
for error, count in sorted(error.items(), key=lambda item: item[1], reverse=True):
    error_sorted.append([error, count])

# El diccionario per_user se debe ordenar por nombre de usuario.
for username in sorted(per_user.keys()):
    user_sorted.append([username, per_user[username]["INFO"], per_user[username]["ERROR"]])

# Insertar los nombres de las columnas ("Error", "Count") en la posición cero del diccionario error_sorted.
error_sorted.insert(0, ["Error", "Count"])
# Insertar los nombres de las columnas ("Username", "INFO", "ERROR") en la posición cero del diccionario user_sorted.
user_sorted.insert(0, ["Username", "INFO", "ERROR"])

# Después de ordenar estos diccionarios, almacenarlos en dos archivos diferentes: error_message.csv y user_statistics.csv.
with open("error_message.csv", "w") as error_msg_file:
    writer = csv.writer(error_msg_file)
    writer.writerows(error_sorted)

with open("user_statistics.csv", "w") as user_statistics_file:
    writer = csv.writer(user_statistics_file)
    writer.writerows(user_sorted)
