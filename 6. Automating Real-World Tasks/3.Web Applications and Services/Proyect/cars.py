#!/usr/bin/env python3

# Importando las bibliotecas necesarias
import emails
import reports 
import json
import locale
import sys
import collections
import operator
import os

# Función para cargar los datos del archivo JSON
def load_data(filename):
  """Carga el contenido de filename como un archivo JSON."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data

# Función para formatear la información del coche en una cadena de texto
def format_car(car):
  """Dado un diccionario de coche, devuelve un nombre con un formato adecuado."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])

# Función para procesar los datos y buscar los máximos
def process_data(data):
  """Analiza los datos, buscando los máximos.

  Devuelve una lista de líneas que resumen la información.
  """
  locale.setlocale(locale.LC_ALL, "C.UTF-8")
  max_revenue = {"revenue": 0}
  max_sales = {"total_sales": 0}
  car_year_sales = collections.defaultdict(int)
  for item in data:
    # Calcular la ganancia generada por este modelo (precio * ventas_totales)
    # Necesitamos convertir el precio de "$1234.56" a 1234.56
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item

    # También gestionamos las ventas máximas
    if item["total_sales"] > max_sales["total_sales"]:
      max_sales = item

    # Agregar las ventas totales al contador del año del coche
    car_year_sales[item["car"]["car_year"]] += item["total_sales"]

  # También gestionamos el año de coche más popular
  popular_car_year = max(car_year_sales.items(), key=operator.itemgetter(1))
  pop_year, pop_sales = popular_car_year

  # Generando el resumen
  summary = [
    "El {} generó la mayor ganancia: ${}".format(format_car(max_revenue["car"]), max_revenue["revenue"]),
    "El {} tuvo la mayor cantidad de ventas: {}".format(format_car(max_sales["car"]), max_sales["total_sales"]),
    "El año más popular fue {} con {} ventas.".format(pop_year, pop_sales)
  ]

  return summary

# Función para convertir el diccionario de coches en una tabla
def cars_dict_to_table(car_data):
  """Convierte los datos en car_data en una lista de listas."""
  table_data = [["ID", "Coche", "Precio", "Ventas Totales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data

# Función principal
def main(argv):
  """Procesa los datos JSON y genera un informe completo a partir de ellos."""
  # Cargando los datos
  data = load_data("car_sales.json")

  # Procesando los datos
  summary = process_data(data)

  # Generando el informe en PDF
  filename = "/tmp/cars.pdf"
    title = "Resumen de ventas del último mes"
  additional_info = "<br/>".join(summary)
  table_data = cars_dict_to_table(data)

  # Utilizamos la biblioteca reports para generar el informe en PDF
  reports.generate(filename, title, additional_info, table_data)

  # Preparando el correo electrónico para enviar el informe
  sender = "automation@example.com"
  recipient = "{}@example.com".format(os.environ.get('USER'))
  subject = "Resumen de ventas del último mes"
  body = "\n".join(summary)
  attachment_path = "/tmp/cars.pdf"

  # Generamos el correo electrónico con la biblioteca emails
  message = emails.generate(sender, recipient, subject, body, attachment_path)

  # Enviamos el correo electrónico
  emails.send(message)
  
# Este código se ejecutará si se lanza este script como el principal
if __name__ == "__main__":
  main(sys.argv)

